import type { ReactNode } from 'react';
import type { ButtonProps, Locale, ThemeTokens } from 'react-liquis-glass';

export interface GlassRootProps extends ThemeTokens {
  locale?: Locale;
  children?: ReactNode;
}
export declare function GlassRoot(props: GlassRootProps): JSX.Element;

export declare function getGlass(): boolean;
export declare function setGlass(on: boolean): void;
export declare function useGlass(): boolean;
export interface GlassToggleProps extends Omit<ButtonProps, 'onClick' | 'children' | 'icon'> {
  compact?: boolean;
}
export declare function GlassToggle(props: GlassToggleProps): JSX.Element;

export type ThemeMode = 'auto' | 'light' | 'dark';
export declare function getThemeMode(): ThemeMode;
export declare function setThemeMode(mode: ThemeMode): void;
export declare function useThemeMode(): ThemeMode;
export declare function ThemeToggle(props: GlassToggleProps): JSX.Element;
