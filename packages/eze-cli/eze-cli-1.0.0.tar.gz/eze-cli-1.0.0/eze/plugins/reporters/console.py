"""Console reporter class implementation"""
from pydash import py_

from eze.core.enums import VulnerabilityType, VulnerabilitySeverityEnum, Vulnerability
from eze.core.reporter import ReporterMeta
from eze.core.tool import ScanResult
from eze.utils.log import log, log_debug, log_error
from eze.utils.scan_result import (
    vulnerabilities_short_summary,
    bom_short_summary,
    name_and_time_summary,
    has_sbom_data,
    has_vulnerability_data,
)
from eze.utils.io.print import pretty_print_table
from eze.utils.license import annotated_sbom_table


class ConsoleReporter(ReporterMeta):
    """Python report class for echoing all output into the console"""

    REPORTER_NAME: str = "console"
    SHORT_DESCRIPTION: str = "standard command line reporter"
    INSTALL_HELP: str = """inbuilt"""
    MORE_INFO: str = """inbuilt"""
    LICENSE: str = """inbuilt"""
    VERSION_CHECK: dict = {"FROM_EZE": True}
    EZE_CONFIG: dict = {
        "PRINT_SUMMARY_ONLY": {
            "type": bool,
            "default": False,
            "help_text": """Whether or not to only print the summary (not bom or vulnerabilities)
defaults to false""",
        },
        "PRINT_IGNORED": {
            "type": bool,
            "default": False,
            "environment_variable": "PRINT_IGNORED",
            "help_text": """Whether or not to print out ignored vulnerabilities
defaults to false""",
        },
        "PRINT_TRANSITIVE_PACKAGES": {
            "type": bool,
            "default": False,
            "environment_variable": "PRINT_TRANSITIVE_PACKAGES",
            "help_text": """print out non top level packages""",
        },
    }

    async def run_report(self, scan_results: list):
        """Method for taking scans and turning then into report output"""
        log("Eze report results:\n")
        scan_results_with_vulnerabilities = []
        scan_results_with_sboms = []
        scan_results_with_warnings = []
        scan_results_with_errors = []
        self.print_scan_summary_table(scan_results)

        if self.config["PRINT_SUMMARY_ONLY"]:
            return

        for scan_result in scan_results:
            if self._has_printable_vulnerabilities(scan_result):
                scan_results_with_vulnerabilities.append(scan_result)
            if has_sbom_data(scan_result):
                scan_results_with_sboms.append(scan_result)
            if len(scan_result.warnings) > 0:
                scan_results_with_warnings.append(scan_result)
            if len(scan_result.fatal_errors) > 0:
                scan_results_with_errors.append(scan_result)

        self._print_scan_report_errors(scan_results_with_errors)
        self._print_scan_report_warnings(scan_results_with_warnings)
        self._print_scan_report_vulnerabilities(scan_results_with_vulnerabilities)
        self._print_scan_report_sbom(scan_results_with_sboms)

    def print_scan_summary_table(self, scan_results: list):
        """Print scan summary as table"""
        sboms = []
        summaries = []
        for scan_result in scan_results:
            run_details = scan_result.run_details
            tool_name = py_.get(run_details, "tool_name", "unknown")
            run_type = f":{run_details['run_type']}" if "run_type" in run_details and run_details["run_type"] else ""
            scan_type = (
                run_details["tool_type"] if "tool_type" in run_details and run_details["tool_type"] else "unknown"
            )
            duration_sec = py_.get(run_details, "duration_sec", "unknown")

            if has_sbom_data(scan_result):
                sboms.append(f"BILL OF MATERIALS: {tool_name}{run_type} (duration: {'{:.1f}s'.format(duration_sec)})")
                sboms.append(f"    {bom_short_summary(scan_result, '    ', self.config['PRINT_TRANSITIVE_PACKAGES'])}")

            entry = {
                "Name": tool_name + run_type,
                "Type": scan_type,
                "Critical": "-",
                "High": "-",
                "Medium": "-",
                "Low": "-",
                "Ignored": "-",
                "Warnings": str(len(scan_result.warnings) > 0) or len(scan_result.fatal_errors) > 0,
                "Time": "{:.1f}s".format(duration_sec),
            }

            if has_vulnerability_data(scan_result):
                entry["Ignored"] = str(scan_result.summary["ignored"]["total"])
                entry["Critical"] = str(scan_result.summary["totals"]["critical"])
                entry["High"] = str(scan_result.summary["totals"]["high"])
                entry["Medium"] = str(scan_result.summary["totals"]["medium"])
                entry["Low"] = str(scan_result.summary["totals"]["low"])
                if len(scan_result.fatal_errors) > 0:
                    entry["Ignored"] = "Error"
                    entry["Critical"] = "Error"
                    entry["High"] = "Error"
                    entry["Medium"] = "Error"
                    entry["Low"] = "Error"
                summaries.append(entry)
        pretty_print_table(summaries, False)
        if len(sboms) > 0:
            log("\n".join(sboms))

    def print_scan_summary_title(self, scan_result: ScanResult, prefix: str = "") -> str:
        """Title of scan summary title"""

        scan_summary = f"""{prefix}TOOL REPORT: {name_and_time_summary(scan_result, "")}\n"""

        # bom count if exists
        if has_sbom_data(scan_result):
            scan_summary += bom_short_summary(scan_result, prefix + "    ", self.config["PRINT_TRANSITIVE_PACKAGES"])

        # if bom only scan, do not print vulnerability count
        if has_vulnerability_data(scan_result):
            scan_summary += vulnerabilities_short_summary(scan_result, prefix + "    ")
        log(scan_summary)

    def _has_printable_vulnerabilities(self, scan_result: ScanResult) -> bool:
        """Method for taking scan vulnerabilities return True if anything to print"""
        if len(scan_result.vulnerabilities) <= 0:
            return False
        if not self.config["PRINT_IGNORED"] and scan_result.summary["totals"]["total"] == 0:
            return False
        return True

    def _print_scan_report_vulnerabilities(self, scan_results_with_vulnerabilities: list):
        """Method for taking scan vulnerabilities and printing them"""

        if len(scan_results_with_vulnerabilities) <= 0:
            return
        log(
            """
Vulnerabilities
================================="""
        )
        for scan_result in scan_results_with_vulnerabilities:
            run_details = scan_result.run_details
            tool_name = py_.get(run_details, "tool_name", "unknown")
            run_type = f":{run_details['run_type']}" if "run_type" in run_details and run_details["run_type"] else ""
            small_indent = "    "
            indent = "        "
            log(
                f"""
{small_indent}[{tool_name}{run_type}] Vulnerabilities
{small_indent}================================="""
            )
            self.print_scan_summary_title(scan_result, "    ")
            vulnerability: Vulnerability = None
            for vulnerability in scan_result.vulnerabilities:
                if vulnerability.is_ignored:
                    # INFO: By Default ignore "ignored vulnerabilities"
                    if self.config["PRINT_IGNORED"]:
                        log(f"""{indent}(ignored)""")
                    else:
                        continue

                severity = VulnerabilitySeverityEnum.normalise_name(vulnerability.severity).upper()
                vulnerability_type = VulnerabilityType.normalise_name(vulnerability.vulnerability_type).upper()
                first_line = f"""{indent}[{severity} {vulnerability_type}] : {vulnerability.name}"""
                if vulnerability.version:
                    first_line += f" ({vulnerability.version})"
                log(first_line)
                log(f"""{indent}overview: {vulnerability.overview}""")
                for identifier_key in vulnerability.identifiers:
                    identifier_value = vulnerability.identifiers[identifier_key]
                    log(f"""{indent}{identifier_key}: {identifier_value}""")

                if vulnerability.recommendation:
                    log(f"""{indent}recommendation: {vulnerability.recommendation}""")

                if vulnerability.file_location:
                    log(
                        f"""{indent}file: {vulnerability.file_location.get('path')}:{vulnerability.file_location.get('line', '1')}"""
                    )
                log("")

    def _print_scan_report_sbom(self, scan_results_with_sboms: list):
        """print scan sbom"""
        if len(scan_results_with_sboms) <= 0:
            return
        log(
            """
Bill of Materials
================================="""
        )
        for scan_result in scan_results_with_sboms:
            run_details = scan_result.run_details
            tool_name = py_.get(run_details, "tool_name", "unknown")
            run_type = f":{run_details['run_type']}" if "run_type" in run_details and run_details["run_type"] else ""
            for project_name in scan_result.sboms:
                cyclonedx_bom = scan_result.sboms[project_name]
                log(
                    f"""
[{tool_name}{run_type}] {project_name} SBOM
================================="""
                )
                sboms = annotated_sbom_table(cyclonedx_bom, self.config["PRINT_TRANSITIVE_PACKAGES"])
                pretty_print_table(sboms)

    def _print_scan_report_warnings(self, scan_results_with_warnings: list):
        """print scan warnings"""
        if len(scan_results_with_warnings) <= 0:
            return

        log(
            """
Warnings
================================="""
        )
        for scan_result in scan_results_with_warnings:
            run_details = scan_result.run_details
            tool_name = py_.get(run_details, "tool_name", "unknown")
            run_type = f":{run_details['run_type']}" if "run_type" in run_details and run_details["run_type"] else ""
            small_indent = "    "
            indent = "        "
            log(
                f"""
{small_indent}[{tool_name}{run_type}] Warnings
{small_indent}================================="""
            )
            for warning in scan_result.warnings:
                log(f"""{indent}{warning}""")

    def _print_scan_report_errors(self, scan_results_with_errors: list):
        """print scan errors"""
        if len(scan_results_with_errors) <= 0:
            return

        log(
            """
Errors
================================="""
        )
        for scan_result in scan_results_with_errors:
            run_details = scan_result.run_details
            tool_name = py_.get(run_details, "tool_name", "unknown")
            run_type = f":{run_details['run_type']}" if "run_type" in run_details and run_details["run_type"] else ""
            small_indent = "    "
            indent = "        "
            log(
                f"""
{small_indent}[{tool_name}{run_type}] Errors
{small_indent}================================="""
            )
            for fatal_error in scan_result.fatal_errors:
                log(f"""{indent}{fatal_error}""")
