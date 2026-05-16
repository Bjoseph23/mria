import localforage from "localforage";

const routeCache = localforage.createInstance({ name: "mria-route-cache" });

export interface CachedRoute {
  route: any;
  timestamp: number;
  origin: string;
  destination: string;
}

export async function getCachedRoute(origin: string, destination: string): Promise<any | null> {
  const key = `${origin.toLowerCase()}->${destination.toLowerCase()}`;
  const cached = await routeCache.getItem<CachedRoute>(key);
  
  if (cached && Date.now() - cached.timestamp < 900_000) { // 15 min TTL
    return cached.route;
  }
  return null;
}

export async function setCachedRoute(origin: string, destination: string, route: any) {
  const key = `${origin.toLowerCase()}->${destination.toLowerCase()}`;
  await routeCache.setItem(key, {
    route,
    timestamp: Date.now(),
    origin,
    destination
  });
}

export async function getAllCachedRoutes(): Promise<CachedRoute[]> {
  const routes: CachedRoute[] = [];
  await routeCache.iterate((value: CachedRoute) => {
    routes.push(value);
  });
  return routes.sort((a, b) => b.timestamp - a.timestamp);
}
