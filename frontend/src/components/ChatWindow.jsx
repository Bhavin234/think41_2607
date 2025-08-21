import React, { useState } from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';
import SessionList from './SessionList';
import './ChatWindow.css';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const onSend = async (text) => {
    const userMessage = { sender: 'user', text };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text })
      });

      const data = await res.json();
      const aiMessage = { sender: 'ai', text: data.response };
      setMessages((prev) => [...prev, aiMessage]);

    } catch (error) {
      console.error('Failed to fetch:', error);
    }
  };

  return (
    <div className="chat-window">
      <div className="sidebar">
        <SessionList />
      </div>
      <div className="main">
        <h1 className="title">E-commerce Chat Support</h1>
        <MessageList messages={messages} />
        <UserInput value={input} onChange={setInput} onSend={onSend} />
      </div>
    </div>
  );
};

export default ChatWindow;
