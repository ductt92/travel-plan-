// Tranh minh họa nền cho hai thẻ trên trang chủ (SVG, các lớp far/mid/near/sun dịch nhẹ khi rê chuột)

export function MapArt() {
  // tấm bản đồ giấy gấp ba nằm trên mặt biển, đường bay nét đứt nối các trái tim
  const heart = 'M0 0 C-3 -4 -11 -7 -11 -14 C-11 -19 -7 -22 -4 -22 C-2 -22 -0.5 -21 0 -19 C0.5 -21 2 -22 4 -22 C7 -22 11 -19 11 -14 C11 -7 3 -4 0 0Z';
  return (
    <svg className="choice__art" viewBox="0 0 600 460" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
      <defs>
        <linearGradient id="mp-sea" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#FCE3D9" /><stop offset=".5" stopColor="#F6C6CF" /><stop offset="1" stopColor="#B9DCE8" /></linearGradient>
        <linearGradient id="mp-paper" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#FFF8EE" /><stop offset="1" stopColor="#F7E7D2" /></linearGradient>
      </defs>
      <rect width="600" height="460" fill="url(#mp-sea)" />
      <g stroke="#FFFFFF" strokeWidth="2" fill="none" opacity=".5" strokeLinecap="round">
        <path d="M30 380 q20 -10 40 0 t40 0" /><path d="M470 60 q20 -10 40 0 t40 0" /><path d="M500 400 q15 -8 30 0 t30 0" />
      </g>
      <g className="far" fill="#FFFFFF" opacity=".7"><path d="M60 80c14-11 34-8 42 3 12-5 26 1 28 12H52c-3-6 2-13 8-15Z" /><path d="M420 120c12-9 28-7 35 2 10-4 22 1 24 10h-66c-2-5 2-10 7-12Z" /></g>
      <g className="mid" transform="rotate(-6 300 230)">
        <path d="M110 70 L230 90 L230 400 L110 380Z" fill="url(#mp-paper)" />
        <path d="M230 90 L360 70 L360 380 L230 400Z" fill="#F3DFC6" />
        <path d="M360 70 L480 90 L480 400 L360 380Z" fill="url(#mp-paper)" />
        <g stroke="#E2C9AE" strokeWidth="1" opacity=".8">
          <path d="M110 150 L480 150 M110 230 L480 230 M110 310 L480 310" /><path d="M170 80 V390 M300 80 V390 M420 80 V390" />
        </g>
        <path d="M250 120 C230 160 270 190 250 230 C235 260 280 290 300 330 C312 352 300 370 320 385" fill="none" stroke="#9FC9B0" strokeWidth="9" strokeLinecap="round" opacity=".55" />
      </g>
      <g className="near">
        <path d="M262 132 Q170 230 330 335" fill="none" stroke="#B8364F" strokeWidth="3" strokeDasharray="8 7" strokeLinecap="round" />
        <path d="M262 132 Q250 118 236 150" fill="none" stroke="#B8364F" strokeWidth="3" strokeDasharray="6 6" strokeLinecap="round" />
        <text x="225" y="245" fontSize="26" fill="#B8364F" transform="rotate(60 225 245)">✈</text>
        <g transform="translate(236 152) scale(1.4)"><path d={heart} fill="#E05A73" stroke="#FFFFFF" strokeWidth="1.5" /></g>
        <g transform="translate(330 340) scale(1.7)"><path d={heart} fill="#E05A73" stroke="#FFFFFF" strokeWidth="1.5" /></g>
        <circle cx="262" cy="132" r="7" fill="#FFFFFF" stroke="#B8364F" strokeWidth="3" />
      </g>
      <g className="sun" transform="translate(520 250)">
        <circle r="34" fill="#FFFFFF" opacity=".75" />
        <path d="M0 -26 L6 0 L0 26 L-6 0Z" fill="#B8364F" /><path d="M-26 0 L0 -6 L26 0 L0 6Z" fill="#E7A9B5" />
        <text y="-31" textAnchor="middle" fontSize="11" fontWeight="700" fill="#B8364F">B</text>
      </g>
    </svg>
  );
}

export function ZhArt() {
  return (
    <>
      <svg className="choice__art" viewBox="0 0 600 460" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <defs>
          <linearGradient id="zh-paper" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#FFF4E0" /><stop offset=".55" stopColor="#F9DDB8" /><stop offset="1" stopColor="#EFB28A" /></linearGradient>
          <radialGradient id="zh-sun"><stop offset="0" stopColor="#E8432F" /><stop offset="1" stopColor="#C8281E" /></radialGradient>
        </defs>
        <rect width="600" height="460" fill="url(#zh-paper)" />
        <g className="sun"><circle cx="150" cy="120" r="62" fill="url(#zh-sun)" opacity=".92" /></g>
        <g className="ink">
          <path d="M-20 300 C40 250 70 190 120 210 C160 226 170 150 220 160 C270 170 260 250 320 240 C380 230 400 170 450 190 C510 214 520 260 640 240 L640 460 L-20 460Z" fill="#3E4A47" opacity=".35" />
          <path d="M-20 340 C60 300 110 260 170 290 C230 320 260 250 330 280 C400 310 440 270 520 300 C570 318 600 300 640 296 L640 460 L-20 460Z" fill="#26413A" opacity=".75" />
          <path d="M-20 390 C80 360 160 372 240 360 C340 344 420 378 520 360 C570 352 610 360 640 356 L640 460 L-20 460Z" fill="#14231F" />
        </g>
        <g stroke="#1C1A17" strokeWidth="3" strokeLinecap="round" fill="none" opacity=".75">
          <path d="M40 300 C60 270 70 250 66 220" /><path d="M66 238 C80 230 92 232 100 240" /><path d="M62 258 C48 252 40 254 32 262" />
        </g>
        <g fill="#1C1A17" opacity=".7">
          <ellipse cx="96" cy="238" rx="12" ry="4" transform="rotate(-20 96 238)" /><ellipse cx="34" cy="260" rx="12" ry="4" transform="rotate(25 34 260)" /><ellipse cx="78" cy="214" rx="10" ry="3.5" transform="rotate(-50 78 214)" />
        </g>
        <g stroke="#1C1A17" strokeWidth="2" fill="none" strokeLinecap="round" opacity=".55"><path d="M250 90 l8 5 8-5" /><path d="M276 80 l6 4 6-4" /></g>
      </svg>
      <span className="choice__callig" aria-hidden="true">学汉语</span>
      <span className="choice__stamp" aria-hidden="true">汉路</span>
    </>
  );
}

export function Hsk6Art() {
  // một tấm slide bài giảng (thanh tím, gạch cam như slide trong video) với nút phát, trên nền kem – tím nhạt
  return (
    <>
      <svg className="choice__art" viewBox="0 0 600 460" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <defs>
          <linearGradient id="h6-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#FBF8F3" /><stop offset=".55" stopColor="#EFE4F3" /><stop offset="1" stopColor="#D9C2E4" /></linearGradient>
        </defs>
        <rect width="600" height="460" fill="url(#h6-bg)" />
        <g className="far" fill="#5B2A6E" opacity=".08"><circle cx="90" cy="90" r="70" /><circle cx="520" cy="380" r="110" /></g>
        <g className="mid" transform="rotate(-5 260 190)">
          <rect x="70" y="70" width="330" height="210" rx="14" fill="#FFFFFF" />
          <path d="M70 84a14 14 0 0 1 14-14h302a14 14 0 0 1 14 14v22H70Z" fill="#5B2A6E" />
          <rect x="70" y="106" width="330" height="4" fill="#DE7028" />
          <g fill="#5B2A6E" opacity=".85"><rect x="96" y="132" width="120" height="12" rx="6" /></g>
          <g fill="#2A2230" opacity=".25"><rect x="96" y="160" width="250" height="8" rx="4" /><rect x="96" y="180" width="210" height="8" rx="4" /><rect x="96" y="200" width="230" height="8" rx="4" /></g>
          <text x="96" y="252" fontSize="30" fill="#DE7028" fontFamily="'Noto Serif SC','Songti SC',serif">wèilái</text>
        </g>
        <g className="near">
          <circle cx="352" cy="262" r="34" fill="#5B2A6E" />
          <circle cx="352" cy="262" r="44" fill="none" stroke="#5B2A6E" strokeWidth="2" opacity=".25" />
          <path d="M342 246 L368 262 L342 278Z" fill="#FFFFFF" />
        </g>
      </svg>
      <span className="choice__callig choice__callig--hsk6" aria-hidden="true">未来</span>
      <span className="choice__stamp choice__stamp--hsk6" aria-hidden="true">六</span>
    </>
  );
}
