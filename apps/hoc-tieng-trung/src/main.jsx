import { createRoot } from 'react-dom/client';
import '@trang/ui/tokens.css';
import { GlassRoot } from '@trang/ui/glass';
import './app.css';
import { App } from './App.jsx';

createRoot(document.getElementById('root')).render(<GlassRoot accent="var(--jade)"><App /></GlassRoot>);
