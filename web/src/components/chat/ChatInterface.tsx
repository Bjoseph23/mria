"use client";

import { CopilotChat } from "@copilotkit/react-ui";
import { MessageSquare, Zap, Shield, Wallet, Search } from "lucide-react";

import { A2UIMessageRenderer } from "./A2UIMessageRenderer";

export function ChatInterface() {
  return (
    <div className="flex-1 flex flex-col h-full bg-black/40 relative overflow-hidden">
      {/* Background decoration */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[600px] h-[600px] bg-primary/10 rounded-full blur-[120px] pointer-events-none" />
      
      <div className="flex-1 overflow-hidden flex flex-col relative z-10">
        <CopilotChat
          labels={{
            title: "mRai",
            initial: "Hujambo! I'm mRai, your Nairobi transit expert. Where are we heading today?",
            placeholder: "Ask follow up or new route...",
          }}
          className="flex-1"
          instructions="You are mRai, a Nairobi transit expert. Use the provided tools to help users find the best matatu routes. Mix in some Sheng/Swahili where natural."
          renderMessage={(props) => <A2UIMessageRenderer {...props} />}
        />
      </div>

      {/* Quick Action Chips */}
      <div className="p-4 flex items-center justify-center gap-3 z-20">
        <button className="flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 bg-white/5 hover:bg-white/10 text-xs font-medium transition-all">
          <Wallet className="w-3 h-3 text-primary" />
          Lowest Fare
        </button>
        <button className="flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 bg-white/5 hover:bg-white/10 text-xs font-medium transition-all">
          <Zap className="w-3 h-3 text-primary" />
          Fastest Path
        </button>
        <button className="flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 bg-white/5 hover:bg-white/10 text-xs font-medium transition-all">
          <Shield className="w-3 h-3 text-primary" />
          Verified Safe
        </button>
      </div>
    </div>
  );
}
