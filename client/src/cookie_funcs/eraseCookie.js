import createCookie from './createCookie.js';

export default function eraseCookie(name) {
  createCookie(name, '', -1);
}
