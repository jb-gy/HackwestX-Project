import React from 'react';
import { Box, Container, Grid, GridItem } from '@chakra-ui/react';
import TransactionSummary from './TransactionSummary';
import BudgetPlanner from './BudgetPlanner';
import ExpenseChart from './ExpenseChart';

const DashboardLayout: React.FC = () => {
  return (
    <Container maxW="container.xl" py={8}>
      <Grid
        templateColumns={{ base: 'repeat(1, 1fr)', lg: 'repeat(3, 1fr)' }}
        gap={6}
      >
        <GridItem colSpan={{ base: 1, lg: 2 }}>
          <ExpenseChart />
        </GridItem>
        <GridItem>
          <TransactionSummary />
        </GridItem>
        <GridItem colSpan={{ base: 1, lg: 3 }}>
          <BudgetPlanner />
        </GridItem>
      </Grid>
    </Container>
  );
};

export default DashboardLayout;
