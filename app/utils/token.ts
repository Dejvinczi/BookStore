import { deleteCookie, getCookie, setCookie } from 'cookies-next';
import { jwtDecode } from 'jwt-decode';

interface Token {
  token_type: 'access' | 'refresh';
  exp: number;
  iat: number;
  user_id: number;
}

export const storeToken = (type: 'access' | 'refresh', token: string) => {
  const tokenType: string = type + 'Token';
  const decodedToken = decodeToken(token) as { exp: number; iat: number };
  setCookie(tokenType, token, { maxAge: decodedToken.exp - decodedToken.iat });
};

export const getToken = (type: 'access' | 'refresh') => {
  const tokenType: string = type + 'Token';
  return getCookie(tokenType);
};

export const removeTokens = () => {
  deleteCookie('accessToken');
  deleteCookie('refreshToken');
};

export const decodeToken = (token: string): Token => {
  return jwtDecode(token);
};
