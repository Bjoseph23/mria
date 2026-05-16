"use client";

import { useCopilotChat } from "@copilotkit/react-core";
import { A2uiSurface } from "@a2ui/react";

export function A2UIMessageRenderer({ message }: { message: any }) {
  const { surfaces } = useCopilotChat();

  return (
    <div className="space-y-4">
      {message.content && (
        <div className="prose prose-invert max-w-none text-sm leading-relaxed">
          {message.content}
        </div>
      )}
      {surfaces
        .filter((s) => s.messageId === message.id)
        .map((surface) => (
          <A2uiSurface key={surface.id} surface={surface} />
        ))}
    </div>
  );
}
