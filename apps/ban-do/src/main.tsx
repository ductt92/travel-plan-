import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { GlassRoot } from '@trang/ui/glass';
import App from './App';
import './styles.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <GlassRoot>
      <App />
    </GlassRoot>
  </StrictMode>,
);
