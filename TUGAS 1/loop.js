
//VARIASI 1: Segitiga Siku-siku
console.log("Variasi 1: Segitiga Siku-siku");
for (let i = 1; i <= 5; i++) {
  let baris = "";
  for (let j = 1; j <= i; j++) {
    baris += "*";
  }
  console.log(baris);
}

//VARIASI 2: Segitiga Terbalik
console.log("Variasi 2: Segitiga Terbalik");
for (let i = 5; i >= 1; i--) {
  let baris = "";
  for (let j = 1; j <= i; j++) {
    baris += "*";
  }
  console.log(baris);
}

//VARIASI 3: Segitiga Sama Kaki (Piramida)
console.log("Variasi 3: Piramida");
for (let i = 1; i <= 5; i++) {
  let spasi = " ".repeat(5 - i);
  let bintang = "*".repeat(2 * i - 1);
  console.log(spasi + bintang);
}

//VARIASI 4: Persegi 
console.log("Variasi 4: Persegi");
for (let i = 1; i <= 5; i++) {
  let baris = "";
  for (let j = 1; j <= 5; j++) {
    baris += "*";
  }
  console.log(baris);
}

//VARIASI 5: Belah Ketupat
console.log("Variasi 5: Belah Ketupat");
// bagian atas
for (let i = 1; i <= 5; i++) {
  let spasi = " ".repeat(5 - i);
  let bintang = "*".repeat(2 * i - 1);
  console.log(spasi + bintang);
}
// bagian bawah
for (let i = 4; i >= 1; i--) {
  let spasi = " ".repeat(5 - i);
  let bintang = "*".repeat(2 * i - 1);
  console.log(spasi + bintang);
}