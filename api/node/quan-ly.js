// Lối vào Vercel cho /api/node/quan-ly, /api/node/tai-khoan và /api/node/ban-hang/* (vercel.json chuyển hai cái sau sang đây kèm ?_api=…).
// Gói Hobby chỉ cho 12 function nên chúng dùng chung function với trang quản lý; logic ở backend/node/catalog.js, accounts.js, banhang/.
import catalog from '../../backend/node/catalog.js';
import accounts from '../../backend/node/accounts.js';
import banHang from '../../backend/node/banhang/index.js';

export default function quanLy(req, res) {
  const u = new URL(req.url, 'http://x');
  const api = req.query?._api || u.searchParams.get('_api');
  if (api === 'ban-hang' || u.pathname.includes('/ban-hang/')) return banHang(req, res);
  const isAccounts = req.query?._api === 'tai-khoan' || u.searchParams.get('_api') === 'tai-khoan' || u.pathname.endsWith('/tai-khoan');
  return (isAccounts ? accounts : catalog)(req, res);
}
