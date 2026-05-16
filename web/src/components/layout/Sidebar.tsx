"use client";

import { MessageSquare, MapPin, AlertCircle, CheckCircle2, Clock } from "lucide-react";

const CROWD_REPORTS = [
  {
    id: 1,
    text: '"111 imekwama Waiyaki"',
    time: "2 mins ago",
    via: "Ma3Route",
    status: "Verified",
    color: "bg-green-500",
  },
  {
    id: 2,
    text: '"Jam mbaya Tao. Avoid Archives area."',
    time: "5 mins ago",
    via: "X Report",
    status: "Urgent",
    color: "bg-red-500",
  },
  {
    id: 3,
    text: '"Ruiru bypass has zero police checks right now."',
    time: "12 mins ago",
    via: "Commuter",
    status: "Info",
    color: "bg-blue-500",
  },
];

export function Sidebar() {
  return (
    <aside className="w-[320px] border-r border-white/10 flex flex-col glass overflow-hidden">
      <div className="p-4 border-b border-white/10">
        <div className="relative aspect-square w-full rounded-2xl overflow-hidden glass-card p-2 group">
          <div className="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10" />
          <div className="absolute bottom-4 left-4 z-20 flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
            <span className="text-[10px] font-bold tracking-widest uppercase">Live: Nairobi Metro</span>
          </div>
          <img 
            src="https://images.unsplash.com/photo-1598124838120-009d5c411ca7?q=80&w=800&auto=format&fit=crop" 
            alt="Nairobi Metro" 
            className="w-full h-full object-cover rounded-xl transition-transform duration-700 group-hover:scale-110"
          />
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-6">
        <div>
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xs font-bold tracking-widest uppercase text-muted-foreground flex items-center gap-2">
              Crowd Intelligence
            </h2>
            <span className="bg-primary/20 text-primary text-[10px] font-bold px-2 py-0.5 rounded-full border border-primary/20">
              LIVE
            </span>
          </div>
          
          <div className="space-y-3">
            {CROWD_REPORTS.map((report) => (
              <div key={report.id} className="p-3 rounded-xl border border-white/5 bg-white/[0.02] hover:bg-white/[0.05] transition-all cursor-pointer group">
                <p className="text-sm font-medium mb-2 group-hover:text-primary transition-colors">
                  {report.text}
                </p>
                <div className="flex items-center justify-between text-[10px] text-muted-foreground">
                  <span>{report.time} via {report.via}</span>
                  <span className={`flex items-center gap-1 font-bold ${report.status === 'Urgent' ? 'text-red-400' : 'text-primary'}`}>
                    <div className={`w-1 h-1 rounded-full ${report.color}`} />
                    {report.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="pt-4 border-t border-white/10">
          <h2 className="text-xs font-bold tracking-widest uppercase text-muted-foreground mb-4">
            Recent Searches
          </h2>
          <div className="space-y-2">
            {["Kawangware → Ruai", "Westlands → CBD", "Eastleigh → Langata"].map((search, i) => (
              <div key={i} className="flex items-center gap-3 text-sm text-muted-foreground hover:text-white transition-colors cursor-pointer py-1">
                <Clock className="w-3.5 h-3.5" />
                {search}
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="p-4 border-t border-white/10 bg-white/[0.02] text-[10px] text-muted-foreground flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-1.5 h-1.5 rounded-full bg-green-500" />
          MCP Tool: vector_search_hits(24)
        </div>
        <span>v2.4.0-stable</span>
      </div>
    </aside>
  );
}
