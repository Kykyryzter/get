x1 = [0, 276.6, 221.36, 174.2, 150.68, 123.72, 108.01, 85.52, 67.51, 46.44, 31.57, 27.89, 23.13]
y1 = [0, 585, 467.5, 367.5, 320, 260, 230, 180, 142.5, 97.5, 65, 60, 47.5]

n = 1
UI = 0
II = 0
UU = 0

for i in range(12):
    UI = UI + x1[n] * y1 [n]
    n = n + 1

UI = UI / 12

n = 1

for i in range(12):
    II = II + x1[n] ** 2
    n = n + 1
II = II / 12

n = 1

for i in range(12):
    UU = UU + y1[n] ** 2
    n = n + 1
UU = UU / 12

R = UI / II

print(R)

q = (1/11*(UU / II -R**2)) ** 0.5

print(q)

sist = max(y1) / max(x1) * ((7.5 / max(y1))** 2 + (0.62 / max(x1)) ** 2) ** 0.5
print(sist)

poln = ((q) ** 2 + (sist) ** 2) ** 0.5
print(poln)

x2 = [0, 229.81, 191.03, 158.67, 144.10, 125.02, 109.39, 95.37, 84.59, 70.16, 59.35, 50.76, 26.784]
y2 = [0, 697.5, 600, 500, 452.5, 395, 345, 300, 265, 222.5, 185, 160, 85]

n = 1
UI = 0
II = 0
UU = 0

for i in range(12):
    UI = UI + x2[n] * y2[n]
    n = n + 1

UI = UI / 12

n = 1

for i in range(12):
    II = II + x2[n] ** 2
    n = n + 1
II = II / 12

n = 1

for i in range(12):
    UU = UU + y2[n] ** 2
    n = n + 1
UU = UU / 12

R = UI / II

print(R)

q = (1/11*(UU / II -R**2)) ** 0.5

print(q)

sist = max(y2) / max(x2) * ((7.5 / max(y2))** 2 + (0.62 / max(x2)) ** 2) ** 0.5
print(sist)
poln = ((q) ** 2 + (sist) ** 2) ** 0.5
print(poln)


x3 = [0, 137.21, 93.46, 80.52, 67.24, 59.79, 52.04, 46.31, 31.312, 28.762, 26.783, 22.099]
y3 = [0, 710, 482.5, 415, 347.5, 310, 270, 240, 160, 147.5, 137.5, 115]

n = 1
UI = 0
II = 0
UU = 0

for i in range(11):
    UI = UI + x3[n] * y3[n]
    n = n + 1

UI = UI / 11

n = 1

for i in range(11):
    II = II + x3[n] ** 2
    n = n + 1
II = II / 11

n = 1

for i in range(11):
    UU = UU + y3[n] ** 2
    n = n + 1
UU = UU / 11

R = UI / II

print(R)

q = (1/10*(UU / II -R**2)) ** 0.5

print(q)

sist = max(y3) / max(x3) * ((7.5 / max(y3))** 2 + (0.62 / max(x3)) ** 2) ** 0.5
print(sist)

poln = ((q) ** 2 + (sist) ** 2) ** 0.5
print(poln)

