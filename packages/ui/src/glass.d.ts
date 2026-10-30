import type { ReactNode } from 'react';
import type { Locale, ThemeTokens } from 'react-liquis-glass';

export interface GlassRootProps extends ThemeTokens {
  locale?: Locale;
  children?: ReactNode;
}
export declare function GlassRoot(props: GlassRootProps): JSX.Element;
