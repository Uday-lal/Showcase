function createRipple(event) {
  const button = event.currentTarget;
  const ripple = document.createElement("span");
  ripple.className = "ripple";
  const diameter = Math.max(button.clientWidth, button.clientHeight);
  const radius = diameter / 2;
  ripple.style.width = `${diameter}px`;
  ripple.style.height = `${diameter}px`;
  ripple.style.left = `${event.clientX - (button.offsetLeft + radius)}px`;
  ripple.style.top = `${event.clientY - (button.offsetTop + radius)}px`;
  const rippleClass = button.getElementsByClassName("ripple")[0];
  if (rippleClass) {
    rippleClass.remove();
  }
  button.appendChild(ripple);
}

const buttons = document.getElementsByTagName("button");
for (let button of buttons) {
  if (button.className === "ripple-btn") {
    button.addEventListener("click", createRipple);
  }
}
