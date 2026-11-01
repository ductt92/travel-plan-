export type Role = 'superadmin' | 'admin' | 'editor' | 'viewer';
export interface AuthUser { id: number; username: string; name: string; role: Role }
export interface Session { token: string; user: AuthUser }

export function getSession(): Session | null;
export function onSessionChange(fn: (s: Session | null) => void): () => void;
export function authHeaders(): Record<string, string>;
export function signIn(username: string, password: string): Promise<string | null>;
export function signOut(): void;
export function refreshSession(): Promise<Session | null>;
