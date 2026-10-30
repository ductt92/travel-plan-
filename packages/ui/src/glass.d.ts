import type { ReactNode } from 'react';
import type { Locale, ThemeTokens } from 'liquidglass-ui';

export interface GlassRootProps extends ThemeTokens {
  locale?: Locale;
  children?: ReactNode;
}
export declare function GlassRoot(props: GlassRootProps): JSX.Element;
