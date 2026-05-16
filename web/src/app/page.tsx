"use client";

import { CopilotKit } from "@copilotkit/react-core";
import { A2UIProvider } from "@a2ui/react";
import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { ChatInterface } from "@/components/chat/ChatInterface";
import { RouteTimeline } from "@/components/route/RouteTimeline";

export default function Home() {
  return (
    <CopilotKit runtimeUrl="/api/copilotkit">
      <A2UIProvider>
        <main className="flex flex-col w-full h-screen">
          <Header />
          <div className="flex flex-1 overflow-hidden">
            <Sidebar />
            <ChatInterface />
            <RouteTimeline />
          </div>
        </main>
      </A2UIProvider>
    </CopilotKit>
  );
}
