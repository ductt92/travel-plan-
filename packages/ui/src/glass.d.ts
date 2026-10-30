import type { ReactNode } from 'react';
import type { ThemeTokens } from 'liquidglass-ui';

export interface GlassRootProps extends ThemeTokens {
  children?: ReactNode;
}
export declare function GlassRoot(props: GlassRootProps): JSX.Element;
