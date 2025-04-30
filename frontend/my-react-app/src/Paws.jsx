import pawImage from "./assets/umbc-official-paw-variations.eps.jpg";
import "./Paws.css";

const NUM_PAWS = 25;

function randomBetween(min, max) {
  return Math.random() * (max - min) + min;
}

function PawConfetti() {
  const paws = Array.from({ length: NUM_PAWS }, (_, i) => {
    const top = randomBetween(-10, 100); // percentage of viewport
    // Modify 'left' logic: Randomly distribute paws between 0% to 100% of the viewport
    const left = randomBetween(i % 2 === 0 ? -5 : 30, i % 2 === 0 ? 70 : 105); // alternate between left and right side
    const size = randomBetween(80, 120); // pixels
    const rotate = randomBetween(0, 270);
    const opacity = randomBetween(0.5, 1);
    const style = {
      top: `${top}vh`,
      left: `${left}vw`,
      width: `${size}px`,
      transform: `rotate(${rotate}deg)`,
      opacity,
    };

    return <img key={i} src={pawImage} alt="paw" className="paw" style={style} />;
  });

  return <div className="paw-confetti">{paws}</div>;
}

export default PawConfetti;
