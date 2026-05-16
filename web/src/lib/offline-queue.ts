import localforage from "localforage";

const queryQueue = localforage.createInstance({ name: "mria-query-queue" });

export async function enqueueOfflineQuery(origin: string, destination: string) {
  const id = Date.now().toString();
  await queryQueue.setItem(id, {
    id,
    origin,
    destination,
    timestamp: Date.now(),
    status: "queued"
  });
  return id;
}

export async function processQueue() {
  if (!navigator.onLine) return;
  
  const keys = await queryQueue.keys();
  for (const key of keys) {
    const query = await queryQueue.getItem<any>(key);
    if (query && query.status === "queued") {
      try {
        // Here you would call your API
        // For example: await fetch("/api/query", { ... })
        console.log(`🚌 Processing offline query: ${query.origin} -> ${query.destination}`);
        await queryQueue.removeItem(key);
      } catch (err) {
        console.error("Failed to process offline query:", err);
      }
    }
  }
}

if (typeof window !== "undefined") {
  window.addEventListener("online", processQueue);
}
