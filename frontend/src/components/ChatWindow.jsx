import React, { useEffect } from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';
import { useChat } from '../context/ChatContext';

const ChatWindow = () => {
  const {
    messages, setMessages,
    conversationId, setConversationId,
    history, setHistory,
    loading, setLoading
  } = useChat();

  // Fetch past conversations from backend
  useEffect(() => {
    fetch("http://localhost:3000/api/conversations")
      .then(res => res.json())
      .then(data => setHistory(data));
  }, []);

  const handleSessionClick = (id) => {
    fetch(`http://localhost:3000/api/conversations/${id}`)
      .then(res => res.json())
      .then(data => {
        setMessages(data.messages);
        setConversationId(id);
      });
  };

  return (
    <div className="chat-window" style={{ display: 'flex', flexDirection: 'row' }}>
      {/* Left panel for history */}
      <div style={{ width: '200px', borderRight: '1px solid #ccc', padding: '12px' }}>
        <h4>Sessions</h4>
        {history.map((conv) => (
          <div
            key={conv.id}
            style={{
              padding: '8px',
              marginBottom: '8px',
              background: conv.id === conversationId ? '#dbeafe' : '#f9fafb',
              cursor: 'pointer',
              borderRadius: '4px'
            }}
            onClick={() => handleSessionClick(conv.id)}
          >
            Conversation #{conv.id}
          </div>
        ))}
      </div>

      {/* Right panel for chat */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        <MessageList messages={messages} />
        <UserInput />
      </div>
    </div>
  );
};

export default ChatWindow;
