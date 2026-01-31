// Homework 1: JavaScript Fundamentals
// Name: YOUR NAME HERE
// Date: 1/30/2026

// ============ PART 1: ARRAY FUNCTIONS ============
const numbers = [10, 5, 8, 12, 3, 7, 15, 2, 9, 6];

function sum(numbers) {
  total = 0;

  for (let i = 0; i < numbers.length; i++) {
    total += numbers[i];
  }

  return total;
}

// ============ TEST YOUR CODE ============
console.log('=== Part 1: Arrays ===');
console.log('Numbers:', numbers);

console.log('Sum:', sum(numbers));
// console.log('Average:', average(numbers));
// console.log('Min:', min(numbers));
// console.log('Max:', max(numbers));

// console.log('\n=== Part 2: Strings ===');
// console.log("capitalize('hello'):", capitalize('hello'));
// console.log("reverse('hello'):", reverse('hello'));
// console.log("countVowels('hello'):", countVowels('hello'));

// console.log('\n=== Part 3: Object ===');
// console.log('Student:', student.name);
// console.log('Grades:', student.grades);
// console.log('Average:', student.getAverage());
// console.log('Honor Roll:', student.isHonorRoll());
