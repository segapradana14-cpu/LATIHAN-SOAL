function tentukanGrade(nilai) {
  if (nilai >= 90) {
    return "A";
  } else if (nilai >= 80) {
    return "B";
  } else if (nilai >= 70) {
    return "C";
  } else if (nilai >= 60) {
    return "D";
  } else {
    return "E";
  }
}

let nilai = 85;
let grade = tentukanGrade(nilai);
console.log("Nilai anda " + grade);