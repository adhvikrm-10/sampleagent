import asyncio
from agents.root_agent import IoTHealthMonitor

class AgentEvaluator:
    async def setup(self):
        self.monitor = IoTHealthMonitor()
        await self.monitor.initialize_session("eval_user", "eval_session")

        async def evaluate_diagnostic_accuracy(self):
            cases = [
                {
                    "name": "Healthy ESP32 device",
                    "query": "Check the health status of device ESP32-A1.",
                    "expected_status_keywords": ["healthy"],
                    "expected_issue_keywords": [],  # should not mention serious issues
                },
                {
                    "name": "Overheating ESP32 device",
                    "query": "Check the health status of device ESP32-A7.",
                    "expected_status_keywords": ["warning", "critical"],
                    "expected_issue_keywords": [
                        "temperature", "overheat", "abnormal temperature", "high temperature"
                    ],
                },
                {
                    "name": "Healthy Arduino device",
                    "query": "Analyze the health of device ARDUINO-B3.",
                    "expected_status_keywords": ["healthy"],
                    "expected_issue_keywords": [],
                },
                {
                    "name": "Unknown device ID",
                    "query": "Check the health status of device ESP32-UNKNOWN.",
                    "expected_status_keywords": ["not found", "unknown", "error"],
                    "expected_issue_keywords": [],
                },
                {
                    "name": "General building health query",
                    "query": "Give me a health overview of all devices in Building A.",
                    "expected_status_keywords": ["ESP32-A1", "ESP32-A7", "overview", "summary"],
                    "expected_issue_keywords": ["ESP32-A7", "temperature"],  # should call out known bad device
                },
            ]

            results = []
            for case in cases:
                response = await self.monitor.query("eval_user", "eval_session", case["query"])
                text = response.lower()

                status_ok = any(kw in text for kw in case["expected_status_keywords"]) if case["expected_status_keywords"] else True
                issues_ok = all(kw in text for kw in case["expected_issue_keywords"])

                passed = status_ok and issues_ok

                results.append(
                    {
                        "name": case["name"],
                        "query": case["query"],
                        "passed": passed,
                        "status_match": status_ok,
                        "issues_match": issues_ok,
                        "response_sample": response[:200],
                    }
                )

            accuracy = sum(1 for r in results if r["passed"]) / len(results)
            return {
                "metric": "diagnostic_accuracy",
                "accuracy": accuracy,
                "test_cases": len(results),
                "details": results,
            }

    async def run_full_evaluation(self):
        await self.setup()
        diagnostic_results = await self.evaluate_diagnostic_accuracy()
        # additional evaluations here
        print("Evaluation complete")

if __name__ == "__main__":
    asyncio.run(AgentEvaluator().run_full_evaluation())
