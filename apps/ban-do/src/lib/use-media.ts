import { useEffect, useState } from 'react';

/** Theo dõi một media query. Lần dựng đầu luôn trả false để server và trình duyệt khớp nhau. */
export function useMedia(query: string) {
  const [match, setMatch] = useState(false);

  useEffect(() => {
    const mq = window.matchMedia(query);
    const sync = () => setMatch(mq.matches);
    sync();
    mq.addEventListener('change', sync);
    return () => mq.removeEventListener('change', sync);
  }, [query]);

  return match;
}
