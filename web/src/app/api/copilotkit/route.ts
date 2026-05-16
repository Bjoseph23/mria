import {
  CopilotRuntime,
  GoogleGenerativeAIChatAdapter,
} from "@copilotkit/runtime";
import { NextRequest } from "next/server";

const googleApiKey = process.env.GOOGLE_API_KEY || "AIzaSyAPlGOH-Ano2pfb9jVJnASlErOLYnBoT0g";

export async function POST(req: NextRequest) {
  const { handleRequest } = new CopilotRuntime();
  
  // Note: We are using Gemini 2.5 Pro via the ChatAdapter for direct integration
  // but we can also route to our FastAPI agent if needed.
  // For the A2UI and multi-agent logic, the FastAPI agent is better.
  // However, CopilotKit can directly use Gemini for the chat part.
  
  const serviceAdapter = new GoogleGenerativeAIChatAdapter({
    apiKey: googleApiKey,
    model: "gemini-2.0-pro-exp-02-05", // Using a stable Pro model
  });

  return handleRequest(req, {
    serviceAdapter,
  });
}
