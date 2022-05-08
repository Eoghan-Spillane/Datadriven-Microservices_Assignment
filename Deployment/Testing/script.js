import http from 'k6/http';
import { check, sleep } from 'k6';
export let options = {
  stages: [
    { duration: '15s', target: 1000 },
    { duration: '30s', target: 3500 },
    { duration: '20s', target: 0 },
  ],
};
export default function() {
  let res = http.get('http://127.0.0.1:30000');
  check(res, { 'status was 200': r => r.status == 200 });
  sleep(1);
}