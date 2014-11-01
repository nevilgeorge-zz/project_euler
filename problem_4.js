// Problem 4

var max = 0,
	product;

for (var i = 999; i > 99; i--) {
	for (var j = 999; j > 99; j--) {
		product = i * j;
		if (product.toString().split('').reverse('').join('') === product.toString()) {
			if (product > max) {
				max = product;
			}
		}
	}
}

console.log(max);
