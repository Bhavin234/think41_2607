import React, { useState } from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = (text) => {
    const newMessages = [
      ...messages,
      { sender: 'user', text },
      { sender: 'ai', text: `You said: ${text}` } // Placeholder response
    ];
    setMessages(newMessages);
  };

  return (
    <div className="chat-window">
      <MessageList messages={messages} />
      <UserInput onSend={handleSend} />
    </div>
  );
};

export default ChatWindow;
