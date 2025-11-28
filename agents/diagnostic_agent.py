from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from tools.device_monitoring_tools import get_device_info, get_sensor_readings, analyze_device_health

device_info_tool = FunctionTool(func=get_device_info)
sensor_readings_tool = FunctionTool(func=get_sensor_readings)
health_analysis_tool = FunctionTool(func=analyze_device_health)

diagnostic_agent = Agent(
    name="diagnostic_agent",
    model="gemini-2.0-flash-exp",
    description="Agent to analyze IoT device health and identify issues.",
    instruction="""Use tools to retrieve device info, sensor data, and perform health analysis.""",
    tools=[device_info_tool, sensor_readings_tool, health_analysis_tool]
)
