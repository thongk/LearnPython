
str = input('input current price:' );
price = float(str);

str = input('input your rmb:' );
rmb = int(str);


buy_count = rmb * 1.14 / price;
buy_count = buy_count - buy_count % 200;

current_cash = 9600 * 19.648;
later_cash = buy_count * price;

current_price = (current_cash + later_cash) / (buy_count + 9600);
print('%.2f' % current_price);
