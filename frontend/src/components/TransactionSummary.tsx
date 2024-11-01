import React from 'react';
import { Box, Heading, VStack, Text, Divider } from '@chakra-ui/react';

const TransactionSummary: React.FC = () => {
  // This will be connected to Plaid API data later
  const mockTransactions = [
    { category: 'Food & Dining', amount: 450.75 },
    { category: 'Transportation', amount: 225.50 },
    { category: 'Shopping', amount: 325.25 },
  ];

  return (
    <Box p={6} bg="white" borderRadius="lg" boxShadow="sm">
      <Heading size="md" mb={4}>Recent Transactions</Heading>
      <VStack spacing={4} align="stretch">
        {mockTransactions.map((transaction, index) => (
          <React.Fragment key={index}>
            <Box display="flex" justifyContent="space-between">
              <Text>{transaction.category}</Text>
              <Text fontWeight="bold">${transaction.amount.toFixed(2)}</Text>
            </Box>
            {index < mockTransactions.length - 1 && <Divider />}
          </React.Fragment>
        ))}
      </VStack>
    </Box>
  );
};

export default TransactionSummary;
