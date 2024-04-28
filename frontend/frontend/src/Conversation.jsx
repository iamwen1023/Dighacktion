
import React from "react";

const Conversation = ({ messages }) => {
  return (
    <div className="conversation">
      <h2>Conversation</h2>
      <div className="conversation-messages">
        <div className='user'>
          <h3>You</h3>
        Y a t-il des données sur l'Intérêt d'un dépistage de la NASH chez l'enfant ou l'ado ? Efficacité de la prise en charge non  médicamenteuse chez l'enfant? l'adulte ? Si oui : comment ? A partir de quel age ? quel fréquence ? Merci

        </div>
        <div className="bot"><h3>Chatbot</h3> Il s'agit d'une excellente question qui suscite beaucoup de débats. La société nord-américaine de gastro-nutrition (publication jointe) suggère un dépistage systématique à partir de 9-11 ans chez les enfants obèses (avec une définition stupide car basée sur les percentiles qui sont différents selon les pays) et ceux en surpoids (toujours avec la même définition stupide) avec des facteurs de risque. Ce dépistage repose sur le dosage des ALAT (SGPT). Elle suggère également une surveillance mais avec un degré d'évidence C (donc très discutable).</div>
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.isUser ? "user" : "bot"}`}
          >
            {message.isUser ? <h3>You</h3> : <h3>Chatbot</h3>}
            {message.text}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Conversation;
