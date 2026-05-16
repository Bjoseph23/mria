"use client";

import React from "react";
import { Bus, MapPin, AlertTriangle, Clock, Wallet } from "lucide-react";

export interface RouteStep {
  instruction: string;
  matatuNumber?: string;
  fare?: string;
  stage?: string;
}

export interface RouteResultCardProps {
  origin: string;
  destination: string;
  steps: RouteStep[];
  warnings?: string[];
  confidence: number;
  totalFare: string;
  totalTime: string;
}

export const RouteResultCard = ({
  origin,
  destination,
  steps,
  warnings,
  confidence,
  totalFare,
  totalTime,
}: RouteResultCardProps) => {
  return (
    <div className="glass-card rounded-2xl overflow-hidden border border-white/10 animate-fade-in w-full max-w-md mx-auto my-4">
      <div className="bg-primary/10 p-4 border-b border-white/10">
        <div className="flex justify-between items-center mb-2">
          <span className="text-[10px] font-bold uppercase tracking-widest text-primary">Generated Route</span>
          <div className="flex items-center gap-2">
            <span className="text-[10px] text-muted-foreground">Confidence:</span>
            <div className="w-16 h-1.5 bg-white/10 rounded-full overflow-hidden">
              <div 
                className="h-full bg-primary transition-all duration-1000" 
                style={{ width: `${confidence * 100}%` }}
              />
            </div>
          </div>
        </div>
        <h3 className="text-lg font-bold font-outfit flex items-center gap-2">
          {origin} <ArrowRight className="w-4 h-4 text-muted-foreground" /> {destination}
        </h3>
      </div>

      <div className="p-4 space-y-4">
        {/* Quick Stats */}
        <div className="grid grid-cols-2 gap-2">
          <div className="flex items-center gap-2 p-2 rounded-xl bg-white/5 border border-white/5">
            <Wallet className="w-4 h-4 text-primary" />
            <span className="text-xs font-bold">{totalFare}</span>
          </div>
          <div className="flex items-center gap-2 p-2 rounded-xl bg-white/5 border border-white/5">
            <Clock className="w-4 h-4 text-primary" />
            <span className="text-xs font-bold">{totalTime}</span>
          </div>
        </div>

        {/* Steps */}
        <div className="space-y-3 relative before:absolute before:left-[11px] before:top-2 before:bottom-2 before:w-[1px] before:bg-white/10">
          {steps.map((step, i) => (
            <div key={i} className="relative pl-7 flex items-start gap-3">
              <div className="absolute left-0 top-1 w-6 h-6 rounded-full bg-black border border-white/20 flex items-center justify-center z-10">
                <span className="text-[10px] font-bold">{i + 1}</span>
              </div>
              <div className="flex-1">
                <p className="text-xs font-medium leading-relaxed">{step.instruction}</p>
                {(step.matatuNumber || step.fare) && (
                  <div className="flex gap-2 mt-1">
                    {step.matatuNumber && (
                      <span className="text-[9px] bg-white/10 px-1.5 py-0.5 rounded border border-white/5 font-mono">
                        #{step.matatuNumber}
                      </span>
                    )}
                    {step.fare && (
                      <span className="text-[9px] text-primary font-bold">KSh {step.fare}</span>
                    )}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>

        {/* Warnings */}
        {warnings && warnings.length > 0 && (
          <div className="p-3 rounded-xl bg-red-500/10 border border-red-500/20 space-y-1">
            {warnings.map((warning, i) => (
              <div key={i} className="flex items-start gap-2 text-[10px] text-red-400 font-medium">
                <AlertTriangle className="w-3 h-3 mt-0.5" />
                {warning}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

const ArrowRight = ({ className }: { className?: string }) => (
  <svg className={className} width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <line x1="5" y1="12" x2="19" y2="12"></line>
    <polyline points="12 5 19 12 12 19"></polyline>
  </svg>
);
