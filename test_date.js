const today = new Date('2026-07-03T12:00:00+02:00'); // Fake today in their timezone
today.setHours(0,0,0,0);
const end = new Date(2026, 6, 3); // 3 lug 2026, month is 0-indexed so 6

console.log("today:", today.toISOString(), "time:", today.getTime());
console.log("end:", end.toISOString(), "time:", end.getTime());
console.log("today <= end:", today <= end);
