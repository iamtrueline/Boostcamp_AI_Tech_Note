## ๐ ๊ธ์ผ ์ง๋ฌธ ๋ชฉ๋ก

- torch.gather์์์ dim์ ์๋ฏธ๋?

  - input๊ณผ index์ dimension์ ๋์ผํด์ผ ํ๋ค. ๋ง์ฝ, input์ด 4x10x15์ด๊ณ , dim = 0์ด๋ฉด, index๋ Nx10x15์ฌ์ผ ํ๋ค. ์ฆ, dim์ผ๋ก ์๋ ฅํ ์ฐจ์์ ์ ์ธํ ๋๋จธ์ง ์ฐจ์์ ๋์ผํด์ผํ๋ค.

- chunk์ 2์ฐจ์ ๋ฐฐ์ด์์์ ๋ณํ์ ์ด๋ป๊ฒ ์ด๋ฃจ์ด์ง๋๊ฐ?
- nn.Linear์์์ ํฌ๊ธฐ ๋ณํ์ ์ด๋ป๊ฒ ํด์ผํ๋๊ฐ?

  - ๊ณผ์ ์์ nn.Linear(2,5)๋ฅผ ์๋ ฅํด์ฃผ๊ฒ๋๋ฉด, ์ด์ ๊ฐ์๊ฐ 2๊ฐ์์ 5๊ฐ๋ก ๋ณํ๋ค.
  - ์ด๋ ๊ฒ ๋๋ ์๋ฆฌ์ ๋ํด์๋ ์ ํํ ์์ง ๋ชปํ๋ค.

- 3์ฐจ์์์ ๋๊ฐํ๋ ฌ์ด๋ฉด ์ ์ก๋ฉด์ฒด์์ ์ ์ฒด์ ๋ํ ๋๊ฐ์ธ์ค ์์๋๋ฐ ์๋๊ฐ?

  - ๋ณธ ๊ณผ์ ์์ 3์ฐจ์์ ๋ํ ๋๊ฐํ๋ ฌ์ ๊ฐ 2์ฐจ์์ ๋ฑ์น๋ก ๋ณด๊ณ , ๊ฐ 2์ฐจ์ ํ๋ ฌ์ ๋ํ ๋๊ฐ์์๋ฅผ ์๋ฏธํ ๊ฒ์ด๋ค.

- expand๋ ์ด๋ป๊ฒ ํ์ฉํ๋ ๊ฒ์ธ๊ฐ?

  - ์ฌ๋ฌ ๋ฐฐ์น๊ฐ ์๋ค๊ณ  ํ์ ๋, ๊ฐ ๋ฐฐ์น๋ง๋ค ๋์ผํ ๊ฐ์ ๋ฐ๋ณตํ์ฌ ๋ํ๋ด์ด์ค๋ค.

## ๐ ์ฃผ๋ณ ๋ฐํ

- ์ง์ ๋

  - ๋ค์ํ ์ด๋ฏธ์ง Dataset๋ณ๋ก ๋ถ๋ฅ ๋ชจ๋ธ์ ์ง์  ๋๋ ค๋ณธ ๊ฒ์ ๋ํ ์ค๋ช์ ์งํ

- ์์ง๋

  - Git-Flow์ ๋ํ์ฌ ๋ค์ ํ ๋ฒ ์๊ธฐ์์ผ์ฃผ์์ผ๋ฉฐ, git ์ฌ์ฉ๋ฒ์ ๋ํ ๋ฐํ ์งํ.
