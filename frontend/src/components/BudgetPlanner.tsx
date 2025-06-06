import React, { useState } from 'react';
import {
  Box,
  Heading,
  Input,
  Button,
  VStack,
  HStack,
  Text,
  Progress,
  useToast,
} from '@chakra-ui/react';

interface BudgetCategory {
  category: string;
  budget: number;
  spent: number;
}

const BudgetPlanner: React.FC = () => {
  const [categories, setCategories] = useState<BudgetCategory[]>([
    { category: 'Food & Dining', budget: 500, spent: 450.75 },
    { category: 'Transportation', budget: 300, spent: 225.50 },
    { category: 'Shopping', budget: 400, spent: 325.25 },
  ]);

  const toast = useToast();


  const handleUpdateBudget = (index: number, value: string) => {
    const newBudget = parseFloat(value);
    
    if (isNaN(newBudget) || newBudget < 0) {
      toast({
        title: 'Invalid Input',
        description: 'Please enter a valid positive number',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    setCategories(prevCategories => 
      prevCategories.map((cat, i) => 
        i === index ? { ...cat, budget: newBudget } : cat
      )
    );

    toast({
      title: 'Budget Updated',
      description: `Budget for ${categories[index].category} has been updated.`,
      status: 'success',
      duration: 3000,
      isClosable: true,
    });
  };

  return (
    <Box p={6} bg="white" borderRadius="lg" boxShadow="sm">
      <Heading size="md" mb={4}>Budget Planner</Heading>
      <VStack spacing={4} align="stretch">
        {categories.map((category, index) => (
          <Box key={index}>
            <HStack justify="space-between" mb={2}>
              <Text fontWeight="bold">{category.category}</Text>
              <HStack spacing={4}>
                <Input
                  type="number"
                  value={category.budget}
                  onChange={(e) => handleUpdateBudget(index, e.target.value)}
                  min="0"
                  step="0.01"
                  width="120px"
                />
                <Text>${category.spent.toFixed(2)} spent</Text>
              </HStack>
            </HStack>
            <Progress
              value={(category.spent / category.budget) * 100}
              colorScheme={category.spent > category.budget ? 'red' : 'green'}
              borderRadius="full"
            />
          </Box>
        ))}
      </VStack>
    </Box>
  );
};

export default BudgetPlanner;
