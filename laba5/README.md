# Задание 05
1. Для данных, хранящихся в реляционной базе PotgreSQL реализуйте шаблон
сквозное чтение и сквозная запись (Пользователь/Клиент …);
2. В качестве кеша – используйте Redis
3. Замерьте производительность запросов на чтение данных с и без кеша с
использованием утилиты wrk https://github.com/wg/wrk изменяя количество
потоков из которых производятся запросы (1, 5, 10)
4. Актуализируйте модель архитектуры в Structurizr DSL
5. Ваши сервисы должны запускаться через docker-compose командой dockercompose up (создайте Docker файлы для каждого сервиса)

With redis:
Running 10s test @ http://host.docker.internal:8000/user/login
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.34ms    2.63ms  41.65ms   72.96% 
    Req/Sec   547.04     31.93   600.00     72.00% 
  5452 requests in 10.01s, 772.01KB read
Requests/sec:    544.72

Running 10s test @ http://host.docker.internal:8000/user/login
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.18ms    2.45ms  31.97ms   69.84%
    Req/Sec   110.36      8.56   131.00     43.00%
  5497 requests in 10.01s, 778.38KB read
Requests/sec:    549.25
Transfer/sec:     77.77KB

Running 10s test @ http://host.docker.internal:8000/user/login
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.25ms    2.54ms  32.91ms   72.90%
    Req/Sec    54.76      5.58    70.00     96.80%
  5476 requests in 10.01s, 775.41KB read
Requests/sec:    547.07
Transfer/sec:     77.47KB

Without redis:
Running 10s test @ http://host.docker.internal:8000/user/login
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    28.85ms    4.82ms  62.77ms   73.64% 
    Req/Sec   347.64     26.13   383.00     84.00% 
  3464 requests in 10.01s, 490.63KB read
Requests/sec:    346.14

Running 10s test @ http://host.docker.internal:8000/user/login
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    29.25ms    4.98ms  55.51ms   74.55%
    Req/Sec    68.30     11.70   262.00     79.04%
  3422 requests in 10.10s, 484.56KB read
Requests/sec:    338.83
Transfer/sec:     47.98KB

Running 10s test @ http://host.docker.internal:8000/user/login
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    29.59ms    4.66ms  55.51ms   71.80%
    Req/Sec    33.76      5.52    50.00     56.00%
  3376 requests in 10.01s, 478.05KB read
Requests/sec:    337.24
Transfer/sec:     47.75KB

# Вариант 1
# Батов Алексей М8О-109СВ-24

