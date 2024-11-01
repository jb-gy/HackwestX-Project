import React from 'react';
import { Box, Heading } from '@chakra-ui/react';
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts';

const ExpenseChart: React.FC = () => {
  // This will be connected to real data later
  const data = [
    { name: 'Food & Dining', value: 450.75 },
    { name: 'Transportation', value: 225.50 },
    { name: 'Shopping', value: 325.25 },
    { name: 'Utilities', value: 180.00 },
    { name: 'Entertainment', value: 150.00 },
  ];

  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8'];

  return (
    <Box p={6} bg="white" borderRadius="lg" boxShadow="sm" h="400px">
      <Heading size="md" mb={4}>Expense Distribution</Heading>
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            labelLine={false}
            outerRadius={120}
            fill="#8884d8"
            dataKey="value"
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </Box>
  );
};

export default ExpenseChart;
