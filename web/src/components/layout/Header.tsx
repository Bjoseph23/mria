"use client";

import { Bus, Bell, History, Settings, User } from "lucide-react";

export function Header() {
  return (
    <header className="flex items-center justify-between px-6 py-4 border-b border-white/10 glass z-50">
      <div className="flex items-center gap-3">
        <div className="bg-primary p-2 rounded-xl shadow-lg shadow-primary/20">
          <Bus className="w-6 h-6 text-white" />
        </div>
        <h1 className="text-xl font-bold font-outfit tracking-tight">
          MataRoute <span className="text-primary">AI</span>
        </h1>
        <nav className="hidden md:flex items-center ml-8 gap-6 text-sm font-medium text-muted-foreground">
          <a href="#" className="text-white">Workspace</a>
          <a href="#" className="hover:text-white transition-colors">Analytics</a>
          <a href="#" className="hover:text-white transition-colors">Network Logs</a>
        </nav>
      </div>

      <div className="flex items-center gap-4">
        <div className="relative">
          <input
            type="text"
            placeholder="Search logs..."
            className="bg-white/5 border border-white/10 rounded-full px-4 py-1.5 text-sm w-64 focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
          />
          <kbd className="absolute right-3 top-1/2 -translate-y-1/2 text-[10px] bg-white/10 px-1.5 py-0.5 rounded border border-white/10 text-muted-foreground">
            ⌘K
          </kbd>
        </div>
        <button className="p-2 hover:bg-white/5 rounded-full transition-colors text-muted-foreground hover:text-white">
          <Bell className="w-5 h-5" />
        </button>
        <button className="p-2 hover:bg-white/5 rounded-full transition-colors text-muted-foreground hover:text-white">
          <History className="w-5 h-5" />
        </button>
        <button className="p-2 hover:bg-white/5 rounded-full transition-colors text-muted-foreground hover:text-white">
          <Settings className="w-5 h-5" />
        </button>
        <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-primary to-accent border border-white/20 overflow-hidden shadow-lg shadow-primary/20">
          <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix" alt="User" />
        </div>
      </div>
    </header>
  );
}
