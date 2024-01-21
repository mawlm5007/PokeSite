import React, { Component, Fragment, useEffect, useState } from "react";
import Header from "./components/Header";
import getCard from "./api";

export const CardContext = React.createContext();

function App() {
  const [card, setCard] = useState();

  useEffect(() => {
    const fetchCard = async () => {
      try {
        const response = await getCard.getInfo();
        setCard(response);
      } catch (err) {
        console.log(err.message);
      }
    }
    fetchCard();
  },[]); // eslint-disable-line react-hooks/exhaustive-deps
  return (
    <div>
      <CardContext.Provider value={{card, setCard}}>
        <Header />
      </CardContext.Provider>
    </div>
  )
}

export default App;