const handleColor = (data) => {
  switch (data[0]) {
    case "water":
      return "#6390F0";

    case "ice":
      return "#96D9D6";

    case "grass":
      return "#7ac74c";

    case "bug":
      return "#a6b91a";

    case "ground":
      return "#e2bf65";

    case "rock":
      return "#b6a136";

    case "electric":
      return "#f7d02c";

    case "ghost":
      return "#735797";

    case "fighting":
      return "#c22e28";

    case "fire":
      return "#ee8130";

    case "poison":
      return "#a33ea1";

    case "flying":
      return "#a98ff3";

    default:
      return "#a8a77a";
  }
};

export default handleColor;
