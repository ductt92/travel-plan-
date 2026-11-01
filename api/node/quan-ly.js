// Lối vào Vercel cho /api/node/quan-ly và /api/node/tai-khoan (vercel.json chuyển /tai-khoan sang đây kèm ?_api=tai-khoan).
// Gói Hobby chỉ cho 12 function nên tài khoản dùng chung function với trang quản lý; logic ở backend/node/catalog.js, accounts.js.
import catalog from '../../backend/node/catalog.js';
import accounts from '../../backend/node/accounts.js';

export default function quanLy(req, res) {
  const u = new URL(req.url, 'http://x');
  const isAccounts = req.query?._api === 'tai-khoan' || u.searchParams.get('_api') === 'tai-khoan' || u.pathname.endsWith('/tai-khoan');
  return (isAccounts ? accounts : catalog)(req, res);
}
