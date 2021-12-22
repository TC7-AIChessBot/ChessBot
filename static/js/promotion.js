var promotionModal = new bootstrap.Modal(
  document.getElementById("promotionModal")
);

const setPromotion = (type) => {
  localStorage.setItem("promotion", type);
  localStorage.setItem("promotionStatus", "true");
};
