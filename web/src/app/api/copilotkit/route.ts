import {
  CopilotRuntime,
  GoogleGenerativeAIAdapter,
  copilotRuntimeNextJSAppRouterEndpoint,
} from "@copilotkit/runtime";
import { NextRequest } from "next/server";

const googleApiKey = 
  process.env.GOOGLE_GENERATIVE_AI_API_KEY || 
  process.env.GOOGLE_API_KEY || 
  "AIzaSyAPlGOH-Ano2pfb9jVJnASlErOLYnBoT0g";

export async function POST(req: NextRequest) {
  const runtime = new CopilotRuntime();
  
  const serviceAdapter = new GoogleGenerativeAIAdapter({
    apiKey: googleApiKey,
    model: "gemini-2.0-pro-exp-02-05", 
  });

  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime,
    serviceAdapter,
    endpoint: "/api/copilotkit",
  });

  return handleRequest(req);
}
