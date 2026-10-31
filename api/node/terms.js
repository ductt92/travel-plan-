// Lối vào Vercel cho /api/node/terms và /api/node/grammar (vercel.json chuyển /grammar sang đây kèm ?_api=grammar).
// Gói Hobby chỉ cho 12 function nên hai API của trang hsk6 dùng chung một function; logic ở backend/node/terms.js, grammar.js.
import terms from '../../backend/node/terms.js';
import grammar from '../../backend/node/grammar.js';

export default function hsk6(req, res) {
  const u = new URL(req.url, 'http://x');
  const isGrammar = req.query?._api === 'grammar' || u.searchParams.get('_api') === 'grammar' || u.pathname.endsWith('/grammar');
  return (isGrammar ? grammar : terms)(req, res);
}
