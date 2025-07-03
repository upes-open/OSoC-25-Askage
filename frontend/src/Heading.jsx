import "./Heading.css";
import icon from "./assets/icon.png"

function Heading() {
  return (
    <div id="heading-container">
      <img className="icon" src={icon} alt="Icon" />
      <div id="heading">ASKAGE</div>
    </div>
  );
}

export default Heading;
