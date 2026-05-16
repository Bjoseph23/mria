"use client";

import { MapPin, ArrowRight, Share2, Phone, Info } from "lucide-react";

export function RouteTimeline() {
  return (
    <aside className="w-[380px] border-l border-white/10 glass flex flex-col overflow-hidden">
      <div className="p-6 border-b border-white/10 flex items-center justify-between">
        <h2 className="text-xl font-bold font-outfit">Route Plan</h2>
        <button className="p-2 hover:bg-white/5 rounded-full transition-colors text-muted-foreground hover:text-white">
          <Share2 className="w-5 h-5" />
        </button>
      </div>

      <div className="p-6 space-y-6 flex-1 overflow-y-auto">
        {/* Stats Row */}
        <div className="grid grid-cols-3 gap-3">
          <div className="glass-card p-3 rounded-xl text-center">
            <span className="text-[10px] text-muted-foreground uppercase font-bold tracking-widest block mb-1">Fare</span>
            <span className="text-sm font-bold">KSh 230</span>
          </div>
          <div className="glass-card p-3 rounded-xl text-center">
            <span className="text-[10px] text-muted-foreground uppercase font-bold tracking-widest block mb-1">Reliability</span>
            <span className="text-sm font-bold text-green-400">94%</span>
          </div>
          <div className="glass-card p-3 rounded-xl text-center">
            <span className="text-[10px] text-muted-foreground uppercase font-bold tracking-widest block mb-1">Time</span>
            <span className="text-sm font-bold">1h 15m</span>
          </div>
        </div>

        {/* Timeline */}
        <div className="relative pl-8 space-y-12 py-4">
          <div className="absolute left-[11px] top-6 bottom-6 w-[2px] bg-gradient-to-b from-primary via-muted to-primary/40" />
          
          <div className="relative group">
            <div className="absolute -left-[28px] top-0 w-6 h-6 rounded-full bg-black border-2 border-primary flex items-center justify-center z-10">
              <div className="w-2 h-2 rounded-full bg-primary" />
            </div>
            <div className="flex justify-between items-start">
              <div>
                <h3 className="font-bold text-sm">Kawangware</h3>
                <p className="text-xs text-muted-foreground mt-1">Board Matatu Route 46/56</p>
              </div>
              <span className="text-[10px] font-mono text-muted-foreground">08:15 AM</span>
            </div>
          </div>

          <div className="relative group">
            <div className="absolute -left-[28px] top-0 w-6 h-6 rounded-full bg-black border-2 border-muted flex items-center justify-center z-10">
              <div className="w-2 h-2 rounded-full bg-muted" />
            </div>
            <div className="flex justify-between items-start">
              <div>
                <h3 className="font-bold text-sm text-muted-foreground">CBD (Archives)</h3>
                <p className="text-xs text-muted-foreground mt-1">Quick Transfer (3 min walk)</p>
              </div>
              <span className="text-[10px] font-mono text-muted-foreground">08:50 AM</span>
            </div>
          </div>

          <div className="relative group">
            <div className="absolute -left-[28px] top-0 w-6 h-6 rounded-full bg-black border-2 border-secondary flex items-center justify-center z-10">
              <div className="w-2 h-2 rounded-full bg-secondary" />
            </div>
            <div className="flex justify-between items-start">
              <div>
                <h3 className="font-bold text-sm">Ruai</h3>
                <p className="text-xs text-muted-foreground mt-1">Route 120 / Superhighway</p>
              </div>
              <span className="text-[10px] font-mono text-muted-foreground">09:30 AM</span>
            </div>
          </div>
        </div>

        {/* Why this route? */}
        <div className="p-4 rounded-2xl bg-primary/5 border border-primary/10 space-y-3">
          <div className="flex items-center gap-2 text-primary">
            <Info className="w-4 h-4" />
            <span className="text-[10px] font-bold uppercase tracking-widest">Why this route?</span>
          </div>
          <p className="text-xs text-muted-foreground leading-relaxed">
            I avoided <span className="text-white">Waiyaki Way</span> due to a reported truck stall. By utilizing the 46/56 connector through Valley Road, we bypass the main gridlock. Transferring at Archives is recommended over Railways to catch the <span className="text-white">120 express</span> before the mid-morning surge.
          </p>
        </div>
      </div>

      <div className="p-6">
        <button className="w-full bg-primary hover:bg-primary/90 text-white font-bold py-4 rounded-2xl flex items-center justify-center gap-3 shadow-lg shadow-primary/20 transition-all active:scale-95">
          <Phone className="w-5 h-5" />
          Export to My Phone
        </button>
      </div>
    </aside>
  );
}
