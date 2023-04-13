function moveImages() {
  const images = document.querySelectorAll('.conejo, .perro');
  
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    
    images.forEach((image, index) => {
      const offset = scrollTop / (index + 1);
      const yPos = -offset + 'px';
      
      image.style.transform = `translateY(${yPos})`;
    });
  });
}

window.onload = () => {
  moveImages();
};
