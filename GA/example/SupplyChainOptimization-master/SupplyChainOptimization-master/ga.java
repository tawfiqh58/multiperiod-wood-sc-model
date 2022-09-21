import java.io.*;
import java.util.*;

class Supplier{
	public int supplierId;
	public int supply_item;
	public int supplier_no;
	public int capacity;
	public int order_cost;
	public int procure_cost;
	public int q_grade;

	public int[] cost;
	public int[] time;

	public Supplier(){
		cost = new int[3];
		time = new int[3];
	}

	public Supplier(int id,int item, int no, int cap, int o_cost, int p_cost, int grade){
		// Setting the supplier data over here.
		// The way you will set the parameters, the same way the data will be generated.
		supplierId = id;
		supply_item = item;
		supplier_no = no;
		capacity = cap;
		order_cost = o_cost;
		procure_cost = p_cost;
		q_grade = grade;

		cost = new int[3];
		time = new int[3];
	}

	public Supplier(Supplier s){

		// This part copies the value of one supplier to another.

		supplierId = s.supplierId;
		supply_item = s.supply_item;
		supplier_no = s.supplier_no;
		capacity = s.capacity;
		order_cost = s.order_cost;
		procure_cost = s.procure_cost;
		q_grade = s.q_grade;

		cost = new int[3];
		time = new int[3];

		if((s.cost).length != (s.time).length){
			System.out.println("Cost and Time array length mismatch.");
		}

		for(int i=0;i<(s.cost).length;i++){
			cost[i] = s.cost[i];
			time[i] = s.time[i];
		}
	}

	public void setCost(int c0, int c1, int c2){

		// This function will set the cost of the supplier to various schemes
		cost[0] = c0;
		cost[1] = c1;
		cost[2] = c2;
	}

	public void setTime(int t0, int t1, int t2){
		// This function will set the time.

		time[0] = t0;
		time[1] = t1;
		time[2] = t2;
	}



	public String toString(){

		// This function prints the supplier data;

		String temp="";

		temp += "Supplier Id: "+supplierId+"\n";
		temp += "Supplier info: \n";
		temp += "Supply Item: "+supply_item+"\n";
		temp += "Supplier Id: "+supplier_no+"\n";
		temp += "Supplier Capacity: "+capacity+"\n";
		temp += "Order cost: "+order_cost+"\n";
		temp += "Procurement Cost: "+procure_cost+"\n";
		temp += "Q grade: "+q_grade+"\n";

		temp += "Scheme 1 details: "+cost[0]+"/"+time[0]+"\n";
		temp += "Scheme 2 details: "+cost[1]+"/"+time[1]+"\n";
		temp += "Scheme 3 details: "+cost[2]+"/"+time[2]+"\n";

		return temp;

	}
}


class schemeElement{

	// This class contains the data of various cheme levels. For example scheme 1 stage1, scheme 2 , stage 2 etc.
	
	public int stage;
	public int start;
	public int end;
	public int cost;
	public int time;

	public schemeElement(int stg,int s, int e, int c, int t){
		// Setting all the stage data here.
		stage = stg;
		start = s;
		end = e;
		cost = c;
		time = t;
	}

	public schemeElement(schemeElement s){
		// Copying data from another stage .

		stage = s.stage;
		start = s.start;
		end = s.end;
		cost = s.cost;
		time = s.time;
	}

	public String toString(){
		// Printing stage informations.

		String temp = "";
		temp += "Stage: "+stage;
		temp += " Start : "+start;
		temp += " End: "+end;
		temp += " Cost: "+cost;
		temp += " Time: "+time+"\n";

		return temp;
	}
} 


class Scheme{

	// This class contains all informations of a scheme. It contains three stages
	// First level to second level
	// Second level to thhird level
	// Third level to customer.

	public int schId ;
	public ArrayList<schemeElement> firstStage;
	public ArrayList<schemeElement> secondStage;
	public ArrayList<schemeElement> thirdStage;

	public Scheme(int id){
		schId = id;
		firstStage = new ArrayList<schemeElement>();
		secondStage = new ArrayList<schemeElement>();
		thirdStage = new ArrayList<schemeElement>();
	}

	public Scheme(Scheme s){
		schId = s.schId;
		firstStage = new ArrayList<schemeElement>(s.firstStage);
		secondStage = new ArrayList<schemeElement>(s.secondStage);
		thirdStage = new ArrayList<schemeElement>(s.thirdStage);
	}

}

class ChromosomeScheme{

	// This class contains the inner schemes of a chromosome.
	// For example in our dataset A chromosome has 3 schemes
	// Therefore, inside the code A chromosome has 3 chromosomeSchemes

	public int schemeId;
	public int numberOfSuppliers;
	public int numberOfCustomers;
	public int[] supplierGeneValues;
	public int[] customerGeneValues;

	public ChromosomeScheme(int id,int num_sup, int num_cus){

		// Setting parameters.
		// Scheme data is stored here
		// Name of the following variables reflect what they do

		schemeId = id;
		numberOfSuppliers = num_sup;
		numberOfCustomers = num_cus;
		supplierGeneValues = new int[num_sup];
		customerGeneValues = new int[num_cus];
	}

	public ChromosomeScheme(ChromosomeScheme c){

		// Copying data from another chromosome.
		// Used in multiple cases in evolution process;

		schemeId = c.schemeId;
		numberOfSuppliers = c.numberOfSuppliers;
		numberOfCustomers = c.numberOfCustomers;
		supplierGeneValues = new int[c.numberOfSuppliers];
		customerGeneValues = new int[c.numberOfCustomers];

		System.arraycopy(c.supplierGeneValues, 0, supplierGeneValues, 0, (c.supplierGeneValues).length);
		System.arraycopy(c.customerGeneValues, 0, customerGeneValues, 0, (c.customerGeneValues).length);
	}

}

class Chromosome{

	// This class is modeled as in Chen's paper
	// A chromosome is basically a solution to the Muti Objective BOSC problem
	// We conduct mutation and crossover on chromosomes to produce new solutions

	public ArrayList<ChromosomeScheme> chromosomeParts;
	
	public int cost;
	public int time;
	public int quality;

	public Chromosome(int numberOfParts, int sup_num, int cus_num){
		
		chromosomeParts = new ArrayList<ChromosomeScheme>();
		for(int i=0;i<numberOfParts;i++){
			chromosomeParts.add(new ChromosomeScheme(i,sup_num,cus_num));
		}
	}

}

class ChromosomeComparator implements Comparator<Chromosome>{

	// This class compares two chromosomes Based on their fitness value.

	public int compare(Chromosome a, Chromosome b){

		double val_a = calculateFitnessValue(a);
		double val_b = calculateFitnessValue(b);

		if(val_a > val_b){
			return -1;
		}
		else if(val_b > val_a){
			return 1;
		}

		return 0;

	}

	// The following function calculates the fitness value of the chromosome.

	public double calculateFitnessValue(Chromosome c){
		
		double ans = 20000000.0;
		
		ans += ( -10 * (double)c.cost );
		ans += (-8595 * (double)c.time);
		ans += (30 * (double)c.quality);

		return ans;
	}
	
}

class GenAlgoObject{

	public ArrayList<Chromosome> population;
	public static ArrayList<Supplier> supplierList;
	public ArrayList<Scheme> schemeList;
	public ArrayList<Integer> demands_list;
	public int demand;
	public double costCoEfficient;
	public double timeCoEfficient;
	public double qualityCoEfficient;

	public GenAlgoObject(int d, ArrayList<Supplier> s_list , ArrayList<Scheme> sch_list , ArrayList<Integer> d_list){
		population = new ArrayList<Chromosome>();
		supplierList = s_list;
		schemeList = sch_list;
		demands_list = d_list;
		demand = d;
		costCoEfficient = -0.4;
		timeCoEfficient = -0.3;
		qualityCoEfficient = 0.3;
	}


	public void initialPopulationGeneration(int popsize){

		// This function generates the initial population for the algorithm.
		// The number of chromosomes in the given population size is specified during running of the program.
		
		int entry = 0;
		
		for(int i =0 ;; i++){
		
			if(entry == popsize){
				break;
			}

			Triplet demands = Utilities.threeWaySplitter(demand);
			ArrayList<Integer> d_l = new ArrayList<Integer>(demands_list); 
		
			Chromosome c = new Chromosome(3,24,4);

			// Generating gene values for scheme 1
			ChromosomeScheme cScheme0 = c.chromosomeParts.get(0);  
			processChromosomeEntry(cScheme0,demands.u, d_l);
	
			// Generating gene values for scheme 2
			ChromosomeScheme cScheme1 = c.chromosomeParts.get(1);
			processChromosomeEntry(cScheme1,demands.v, d_l);

			// Generating gene values for scheme 3
			ChromosomeScheme cScheme2 = c.chromosomeParts.get(2);  
			processChromosomeEntry(cScheme2,demands.w, d_l);

			c.cost = calculateCost(c);
			c.time = calculateTime(c);
			c.quality = calculateQualityGrade(c);

			// Adding the generated chromosome to the population.

			population.add(c);
			entry++;
		}

		// Sorting the populations based on elitist preservation method as in chen's paper
		Collections.sort(population, new ChromosomeComparator());
	}

	public void processChromosomeEntry(ChromosomeScheme cScheme0, int schemeOutput, ArrayList<Integer> d_l){

		// This function takes a chromosomeScheme as input and process the data in it
		// The first stage of processing involves checking whether all values are within the supplier capacity limit
		// The second stage of processing involves whether demand = supply condition is met
		// The third stage of processing involves is the customer demand is fully met.

		for(int j=0; j < 24 ; j+= 3){
			
			Triplet allocations = Utilities.threeWaySplitter(schemeOutput);

			int remainingPrev = 0;

			Supplier s0 = supplierList.get(j);

			if(s0.capacity >= allocations.u){
				cScheme0.supplierGeneValues[j] = allocations.u;
			}
			else{
				remainingPrev = allocations.u - s0.capacity;
				cScheme0.supplierGeneValues[j] = s0.capacity;
			}

			Supplier s1 = supplierList.get(j+1);

			if(s1.capacity >= allocations.v+remainingPrev){
				cScheme0.supplierGeneValues[j+1] = allocations.v+remainingPrev;
				remainingPrev = 0;
			}
			else if(s1.capacity >= allocations.v  && (s1.capacity < allocations.v+remainingPrev)){
				cScheme0.supplierGeneValues[j+1] = s1.capacity;
				remainingPrev = remainingPrev - (s1.capacity - allocations.v); 
			}
			else{
				cScheme0.supplierGeneValues[j+1] = s1.capacity;
				remainingPrev = remainingPrev + (allocations.v - s1.capacity) ; 
			}

			Supplier s2 = supplierList.get(j+2);

			if(s2.capacity >= allocations.w+remainingPrev){
				cScheme0.supplierGeneValues[j+2] = allocations.w+remainingPrev;
				remainingPrev = 0;
			}
			else if(s2.capacity >= allocations.w  && (s2.capacity < allocations.w+remainingPrev)){
				cScheme0.supplierGeneValues[j+2] = s2.capacity;
				remainingPrev = remainingPrev - (s2.capacity - allocations.w); 
			}
			else{
				cScheme0.supplierGeneValues[j+2] = s2.capacity;
				remainingPrev = remainingPrev + (allocations.w - s2.capacity) ; 
			}

		}

		int[] d = Utilities.fourWaySplitter(schemeOutput);
		
		for(int j=0;j<4;j++){
			cScheme0.customerGeneValues[j] = 0;
		}

		for(int j=0;j<4;j++){

			int val = (int)d_l.get(j);
			int remainingDemands = 0;

			if(val >= d[j]){
				val = val - d[j];
				cScheme0.customerGeneValues[j] += d[j];
				d_l.set(j,new Integer(val));
			}
			else{
				cScheme0.customerGeneValues[j] += val;
				remainingDemands = d[j] - val;
				val = 0;
				d_l.set(j,new Integer(val));
				for(int k=0;k<4;k++){

					if(remainingDemands == 0){
						break;
					}
					if(k != j){

						int nval = (int)d_l.get(k);
						if(nval >= remainingDemands){
							nval = nval - remainingDemands;
							cScheme0.customerGeneValues[k] += remainingDemands;
							remainingDemands = 0;
							d_l.set(k,new Integer(nval));
						}
						else{
							remainingDemands = remainingDemands - nval;
							cScheme0.customerGeneValues[k] += nval;
							
							d_l.set(k,new Integer(0));
						}
					}
				}
			}
		}
	}


	public int calculateCost(Chromosome c){

		// In this function when a chromosome is given as input, the cost is produced as output
		// The formula used for this function is given in Chen's paper
		
		int cost = 0;

		for(int i=0;i<c.chromosomeParts.size(); i++){

			ChromosomeScheme cs = c.chromosomeParts.get(i);

			for(int j=0; j<24; j++){

				Supplier s = supplierList.get(j);

				if(cs.supplierGeneValues[j] > 0){
					cost += (double)s.order_cost;
				}

				cost += (cs.supplierGeneValues[j] * s.cost[i] );
				cost += (cs.supplierGeneValues[j] * s.procure_cost);
			}

			int totalProduction = 0;
			
			for(int k = 0; k<4 ; k++){
				totalProduction += cs.customerGeneValues[k];
			}

			Scheme sch =  schemeList.get(i);

			for(int k=0; k<sch.firstStage.size() ; k++){

				cost += (totalProduction * sch.firstStage.get(k).cost);
			}

			for(int k=0; k<sch.secondStage.size() ; k++){

				cost += (totalProduction * sch.secondStage.get(k).cost);
			}

			for(int k=0; k<sch.thirdStage.size() ; k++){

				cost += (totalProduction * sch.thirdStage.get(k).cost);
			}

		}

		return cost;
	}

	public int calculateTime(Chromosome c){

		// Given a Chromosome , this function calculates the time involved in the tranportation.
		// The formula used for this is available in Chen's paper
		
		int totalTime = 0;
		int total_demand = 0;

		int[] scheme_time = new int[3];
		int[] productions = new int[3];

		for(int i=0;i<demands_list.size();i++){
			total_demand += demands_list.get(i);
		}

		for(int i=0;i<3;i++){

			int schemeTime = 0;

			ChromosomeScheme cs = c.chromosomeParts.get(i);

			int supplierToFirstStage = 0;

			for(int j=0;j<24;j++){
				
				if(cs.supplierGeneValues[j] > 0){

					supplierToFirstStage = max(supplierToFirstStage, supplierList.get(j).time[i]);

				}
			}

			schemeTime += supplierToFirstStage;
			
			Scheme sch = schemeList.get(i);

			int firstToSecondStage = 0;


			for(int k=0;k<sch.firstStage.size();k++){
				firstToSecondStage = max(firstToSecondStage, sch.firstStage.get(k).time);
			}

			schemeTime += firstToSecondStage;

			int secondToThirdStage = 0;

			for(int k=0;k<sch.secondStage.size();k++){
				secondToThirdStage = max(secondToThirdStage, sch.secondStage.get(k).time);
			}

			schemeTime += secondToThirdStage;

			int thirdStageToCustomer = 0;

			for(int k=0;k<sch.thirdStage.size();k++){
				thirdStageToCustomer = max(thirdStageToCustomer, sch.thirdStage.get(k).time);
			}

			schemeTime += thirdStageToCustomer;

			scheme_time[i] = schemeTime;
			int production = 0;
			for(int k=0;k<4;k++){
				production += cs.customerGeneValues[k];
			}

			productions[i] = production;

		}

		for(int i=0;i<3;i++){
			totalTime += (productions[i] * scheme_time[i]);
		}

		totalTime = (int)Math.round((double)totalTime/(double)total_demand);

		return totalTime;

	}

	public int calculateQualityGrade(Chromosome c){

		// This function calculates the quality grades of the products of a supply chain
		// Formula is given in Chens paper.
		int qg = 0;

		for(int i=0;i<c.chromosomeParts.size();i++){

			ChromosomeScheme cs = c.chromosomeParts.get(i);

			for(int j=0; j<24; j++){
				qg += (cs.supplierGeneValues[j] * supplierList.get(j).q_grade);
			}
			
		}

		return qg;
	}

	public static int lossCalculator(Chromosome c){

		// Calculates the lossValue of a given solution.
		
		int lossValue; 

		int weight = 0;
		int weightedSum = 0;


		for(int i=0; i<c.chromosomeParts.size(); i++){
			ChromosomeScheme cs = c.chromosomeParts.get(i);

			for(int k=0;k<24;k++){
				weight+= cs.supplierGeneValues[k];
				weightedSum += cs.supplierGeneValues[k] * supplierList.get(k).q_grade;
			}
		}

		double temp = (double)weightedSum/(double)(10*weight);

		temp = 64.0/ (temp*temp); 
		lossValue = (int) temp;
		return lossValue;
	}


	public void singleSchemeMutationProcess(Chromosome c){

		// This function takes a chrmomosome as input
		// It mutates the value of the chromosome
		// First it randomly selects a scheme among the chromosomeschemes
		// Then it mutates the value by randomly adding and subtracting value as described in chen's paper
		// After that the chromosomeScheme goes through an equilibrium process
		// The equilibrium process restores the demand = supply condition.

		Chromosome mutatedChromosome = new Chromosome(3,24,4);

		for(int i=0;i<3;i++){
			mutatedChromosome.chromosomeParts.set(i,new ChromosomeScheme(c.chromosomeParts.get(i)));
		}

		Random r = new Random();

		int index = (int)Math.abs(r.nextInt(3));

		ChromosomeScheme toBeMutated = mutatedChromosome.chromosomeParts.get(index);

		for(int i=0;i<24;i+=3){
			int temp_sum = 0;
			
			temp_sum += toBeMutated.supplierGeneValues[i];
			temp_sum += toBeMutated.supplierGeneValues[i+1];
			temp_sum += toBeMutated.supplierGeneValues[i+2];

			if(temp_sum == 0){
				continue;
			}

			Triplet t_x = Utilities.threeWaySplitter(temp_sum);

			int h = highestPriceIndicator(index,i,i+1,i+2);
			int l = lowestPriceIndicator(index,i,i+1, i+2);

			int[] val = {t_x.u, t_x.v, t_x.w};
			Arrays.sort(val);

			if(h == i){
				toBeMutated.supplierGeneValues[i] = val[0];
			}
			else if(l == i){
				toBeMutated.supplierGeneValues[i] = val[2];
			}
			else{
				toBeMutated.supplierGeneValues[i] = val[1];
			}

			if(h == i+1){
				toBeMutated.supplierGeneValues[i+1] = val[0];
			}
			else if(l == i+1){
				toBeMutated.supplierGeneValues[i+1] = val[2];
			}
			else{
				toBeMutated.supplierGeneValues[i+1] = val[1];
			}

			if(h == i+2){
				toBeMutated.supplierGeneValues[i+2] = val[0];
			}
			else if(l == i+2){
				toBeMutated.supplierGeneValues[i+2] = val[2];
			}
			else{
				toBeMutated.supplierGeneValues[i+2] = val[1];
			}
		}

		// Calculating cost , time and quality of the newly generated mutated chromosome

		mutatedChromosome.cost = calculateCost(mutatedChromosome);
		mutatedChromosome.time = calculateTime(mutatedChromosome);
		mutatedChromosome.quality = calculateQualityGrade(mutatedChromosome);

		// Adding the chromosome to the population

		population.add(mutatedChromosome);

	}

	public void crossOverEquilibrium(Chromosome a, Chromosome b){

		// This function takes two chromosomes as input
		// As output gives two chromosomosomes that are results from crossover between inputs
		// The chromosome crossover procedure is explained in Chen's paper
		// First a random scheme from both chromosomes are selected
		// Then they are swapped
		// After that they go through an equilibrium process to meet the demand = supply condition

		Random r = new Random();
		int index = Math.abs(r.nextInt(3));

		ChromosomeScheme c_a = new ChromosomeScheme(a.chromosomeParts.get(index));
		ChromosomeScheme c_b = new ChromosomeScheme(b.chromosomeParts.get(index));

		int a_val = 0;
		int b_val = 0;

		for(int i=0;i<4;i++){
			a_val += c_a.customerGeneValues[i];
			b_val += c_b.customerGeneValues[i];
		}

		double a_ratio = (double)a_val/(double)b_val;
		double b_ratio = (double)b_val/(double)a_val;

		Chromosome crossA = new Chromosome(3,24,4);
		Chromosome crossB = new Chromosome(3,24,4);

		for(int i=0;i<3;i++){
			crossA.chromosomeParts.set(i,b.chromosomeParts.get(i));
			crossB.chromosomeParts.set(i,a.chromosomeParts.get(i));
		}

		crossA.chromosomeParts.set(index,c_b);
		crossB.chromosomeParts.set(index,c_a);

		// Crossover complete
		// Equilibrium process starts here.

		equilibriumProcess(crossA, index, a_ratio);
		equilibriumProcess(crossB, index, b_ratio);

		// Equilibrium complete.
		// Assigning cost now
		crossA.cost = calculateCost(crossA);
		crossB.cost = calculateCost(crossB);
		//Assigning time now
		crossA.time = calculateTime(crossA);
		crossB.time = calculateCost(crossB);
		// Assigning quality now.
		crossA.quality = calculateQualityGrade(crossA);
		crossB.quality = calculateQualityGrade(crossB);
		// Adding them to population.
		population.add(crossA);
		population.add(crossB);
		// Entire crossover complete.
	}

	public void equilibriumProcess(Chromosome c, int x, double ratio){

		ChromosomeScheme cs = c.chromosomeParts.get(x);

		// Scheme data scaling starts ;
		for(int i=0;i<24; i++){
			cs.supplierGeneValues[i] = (int)Math.round((double)cs.supplierGeneValues[i] * ratio);
		}

		int demand_now = 0;

		for(int i=0;i<4; i++){
			cs.customerGeneValues[i] = (int)Math.round((double)cs.customerGeneValues[i] * ratio);
			demand_now += cs.customerGeneValues[i];
		}

		for(int i=0; i<24; i+=3){

			int supply_now = cs.supplierGeneValues[i]+cs.supplierGeneValues[i+1]+cs.supplierGeneValues[i+2];
			int diff = 0;

			if(supply_now<demand_now){

				diff = demand_now  - supply_now;

				int p = lowestPriceIndicator(x, i, i+1, i+2);

				cs.supplierGeneValues[p] = cs.supplierGeneValues[p] + diff;
			}
			else if(supply_now > demand_now){
				
				diff = supply_now - demand_now;

				if(cs.supplierGeneValues[i] - diff >=0){
					cs.supplierGeneValues[i] = cs.supplierGeneValues[i] - diff;
				}
				else if(cs.supplierGeneValues[i+1] - diff >=0){
					cs.supplierGeneValues[i+1] = cs.supplierGeneValues[i+1] - diff;
				}
				else if(cs.supplierGeneValues[i+2] - diff >=0){
					cs.supplierGeneValues[i+2] = cs.supplierGeneValues[i+2] - diff;
				}
			}
		}

		// Scheme data scaling ends;

		// Finding out how much mismatch has occured during crossover.

		int[] deficits = new int[4];


		for(int i=0; i<4; i++){

			int temp_sum = 0;
			temp_sum += c.chromosomeParts.get(0).customerGeneValues[i];
			temp_sum += c.chromosomeParts.get(1).customerGeneValues[i];
			temp_sum += c.chromosomeParts.get(2).customerGeneValues[i];

			deficits[i] = temp_sum - demands_list.get(i);
		}

		// For each mismatch demand = supply condition must be individually met
		// The following loop makes sure that all gene values meet the condition

		for(int i=0;i<4; i++){
			
			int target = deficits[i];
			int k = 0;
			Random r = new Random();
			int iteration = 0;
			while(true){

				do{
					k = Math.abs(r.nextInt(3));
				}while(k != x);

				ChromosomeScheme cx = c.chromosomeParts.get(k);

				if(target > 0){
					
					if(cx.customerGeneValues[i] >= target){
						
						cx.customerGeneValues[i] = cx.customerGeneValues[i] - target;

						for(int j=0; j<24; j+=3){
							int t = target;

							if(cx.supplierGeneValues[j]>=t){
								cx.supplierGeneValues[j] = cx.supplierGeneValues[j]-t;
								continue;
							}
							else{
								t = t - cx.supplierGeneValues[j];
								cx.supplierGeneValues[j] = 0;
							}


							if(cx.supplierGeneValues[j+1]>=t){
								cx.supplierGeneValues[j+1] = cx.supplierGeneValues[j+1]-t;
								continue;
							}
							else{
								t = t - cx.supplierGeneValues[j+1];
								cx.supplierGeneValues[j+1] = 0;
							}


							if(cx.supplierGeneValues[j+2]>=t){
								cx.supplierGeneValues[j+2] = cx.supplierGeneValues[j+2]-t;
								continue;
							}
							else{
								t = t - cx.supplierGeneValues[j+2];
								cx.supplierGeneValues[j+2] = 0;
							}
						}
						break;
					}
					else{
						continue;
					}

				}
				else if(target < 0){
					int t = -target;
					cx.customerGeneValues[i] += t;

					for(int j=0; j<24; j+=3){
						int l = lowestPriceIndicator(k,j,j+1,j+2);
						cx.supplierGeneValues[l] += t;
					}
				}

				iteration++;
				if(iteration == 50){
					break;
				}
			}
		}

	}

	public int lowestPriceIndicator(int s,int x,int y, int z){

		// This function takes 3 suppliers as input and one scheme as input
		// As output it returns which one has the lowest cost to a scheme

		if(supplierList.get(x).cost[s] < supplierList.get(y).cost[s]){
			if(supplierList.get(x).cost[s] < supplierList.get(z).cost[s]){
				return x;
			}
			else{
				return z;
			}
		}
		else{
			if(supplierList.get(y).cost[s] < supplierList.get(z).cost[s]){
				return y;
			}
			else{
				return z;
			}
		}
	}

	public int highestPriceIndicator(int s, int x,int y, int z){

		// This function takes 3 suppliers as input and one scheme as input
		// As output it returns which one has the highest cost to a scheme

		if(supplierList.get(x).cost[s] > supplierList.get(y).cost[s]){
			if(supplierList.get(x).cost[s] > supplierList.get(z).cost[s]){
				return x;
			}
			else{
				return z;
			}
		}
		else{
			if(supplierList.get(y).cost[s] > supplierList.get(z).cost[s]){
				return y;
			}
			else{
				return z;
			}
		}
	}
	

	public void evolutionProcess(int generationNUmber,int inPopSize,int cross_rate, int mutate_rate){

		// This is the main function of the genetic algorithm.
		// This is where genetic algorithm uses crossover and mutations to produce new population
		// These new population is integrated with the old population
		// They are sorted based on their fitness value.
		// The top one third is kept for next phase of iteration while the bottom two third is discarded.

		int presentSize = inPopSize -1;

		double c_r = (double)cross_rate/100.0;
		double m_r = (double)mutate_rate/100.0;

		int cross_number = (int)Math.round((double)presentSize*c_r);
		int mutate_number = (int)Math.round((double)presentSize*m_r);
		mutate_number = 50*mutate_number;
		for(int k=0; k<generationNUmber; k++){
			
			
			Random r = new Random();

			while(true){

				if(cross_number == 0 && mutate_number == 0){
					break;
				}
				
				if(cross_number > 0 ){
					int index1 = (int)Math.abs(r.nextInt(presentSize));
					int index2 = (int)Math.abs(r.nextInt(presentSize));

					crossOverEquilibrium(population.get(index1),population.get(index2));
					cross_number--;
				}
				if(mutate_number > 0 ){
					int index = (int)Math.abs(r.nextInt(presentSize));
					singleSchemeMutationProcess(population.get(index));
					mutate_number--;
				}
			}

			Collections.sort(population,new ChromosomeComparator());
			for(int j = population.size()-1; j>inPopSize-1;j--){
				population.remove(j);
			}
		}
	}	

	public int max(int a,int b){ 
		// Returns the greater between two integers
		return (a>b)?a:b;
	}

	public int min(int a,int b){
		// Returns the minimum between two integers
		return (a<b)?a:b;
	}

}

class Triplet{
	public int u;
	public int v;
	public int w;

	public Triplet(int a,int b, int c){
		u = a; 
		v = b;
		w = c;
	}

	public Triplet(Triplet t){
		u = t.u;
		v = t.v;
		w = t.w;
	}
}

class Utilities{

	public static void printSupplierList(ArrayList<Supplier> s_list){
		
		for(int i=0;i<s_list.size(); i++){
			System.out.println(s_list.get(i));
		}

	}

	public static void demandInput(String filename,ArrayList<Integer> d_list){
		try{
			BufferedReader br = new BufferedReader(new FileReader(filename));
			String line = null;
			while((line = br.readLine()) != null){
				d_list.add(Integer.parseInt(line));
			}
		}catch(IOException ioe){
			ioe.printStackTrace();
		}
	}

	public static int[] fourWaySplitter(int supply){
		Random r = new Random();

		int a = Math.abs(r.nextInt(supply));
		int b = Math.abs(r.nextInt(supply));
		int c = Math.abs(r.nextInt(supply));
		int d = Math.abs(r.nextInt(supply));

		int sum = a+b+c+d;

		double p1 = (double)a/(double)sum;
		double p2 = (double)b/(double)sum;
		double p3 = (double)c/(double)sum;
		double p4 = (double)d/(double)sum;

		int d1 = (int)Math.round((double)supply*p1);
		int d2 = (int)Math.round((double)supply*p2);
		int d3 = (int)Math.round((double)supply*p3);
		int d4 = (int)Math.round((double)supply*p4);

		if((d1+d2+d3+d4) > supply){
			int diff = (d1+d2+d3+d4) - supply;

			if(d1>diff){
				d1 = d1-diff;
			}
			else if(d2>diff){
				d2 = d2-diff;
			}
			else if(d3 > diff){
				d3 = d3-diff;
			}
			else if(d4>diff){
				d4 = d4-diff;
			}
		}

		if((d1+d2+d3+d4) < supply){
			int diff =  supply - (d1+d2+d3+d4);

			d1 += diff;
		}

		if((d1+d2+d3+d4) != supply){
			System.out.println("Quadruplet mismatch.");
		}
		

		int[] result = new int[4];
		result[0] = d1;
		result[1] = d2;
		result[2] = d3;
		result[3] = d4;

		return result;

	}


	public static Triplet threeWaySplitter(int d){

		Random r = new Random();

		int a = Math.abs(r.nextInt(d)+1);
		int b = Math.abs(r.nextInt(d)+1);
		int c = Math.abs(r.nextInt(d)+1);
		
		int sum = a+b+c;

		double p1 = (double)a/(double)sum;
		double p2 = (double)b/(double)sum;
		double p3 = (double)c/(double)sum;

		int d1 = (int)Math.round((double)d*p1);
		int d2 = (int)Math.round((double)d*p2);
		int d3 = (int)Math.round((double)d*p3);

		//System.out.println("d1,d2,d3,d: "+d1 + ","+ d2 +"," + d3+","+d);

		if((d1+d2+d3) > d){
			int diff = (d1+d2+d3) - d;
			

			if(d1>d2){
				if(d1>d3){
					d1 = d1-diff;
				}
				else{
					d3 = d3-diff;
				}
			}
			else{
				if(d2>d3){
					d2 = d2-diff;
				}
				else{
					d3 = d3-diff;
				}
			}
		}
		else if((d1+d2+d3)<d){
			int diff = d - (d1+d2+d3);
			d1 = d1+ diff;
		}		

		if((d1+d2+d3) != d){
			System.out.println("Triplet mismatch.");
		}

		return new Triplet(d1,d2,d3);

	}

	public static void supplierInput(String filename, ArrayList<Supplier> s_list){
		try{
			BufferedReader br = new BufferedReader(new FileReader(filename));
			String line;
			while((line = br.readLine()) != null){
				
				StringTokenizer tk = new StringTokenizer(line);
				
				int id = Integer.parseInt(tk.nextToken());
				int item = Integer.parseInt(tk.nextToken());
				int no = Integer.parseInt(tk.nextToken());
				int capacity = Integer.parseInt(tk.nextToken());
				int o_cost = Integer.parseInt(tk.nextToken());
				int p_cost = Integer.parseInt(tk.nextToken());
				int grade = Integer.parseInt(tk.nextToken());

				int c1 = Integer.parseInt(tk.nextToken());
				int t1 = Integer.parseInt(tk.nextToken());

				int c2 = Integer.parseInt(tk.nextToken());
				int t2 = Integer.parseInt(tk.nextToken());

				int c3 = Integer.parseInt(tk.nextToken());
				int t3 = Integer.parseInt(tk.nextToken());

				Supplier s = new Supplier(id,item, no, capacity, o_cost, p_cost, grade);
				s.setCost(c1, c2, c3);
				s.setTime(t1, t2, t3);

				s_list.add(s);
			}
		}catch(IOException ioe){
			ioe.printStackTrace();
		}
	}

	public static void schemeInput(String filename, ArrayList<Scheme> schemes){
		
		try{
		
			BufferedReader br = new BufferedReader(new FileReader(filename));
			String line;
			int schemeIndex = 0;
			while((line = br.readLine())!= null){

				if(line.equals("Scheme Begins:")){

					Scheme s = new Scheme(schemeIndex);
					schemeIndex++;
					line = br.readLine();

					while(line.equals("Scheme Ends.") == false){

						StringTokenizer tk = new StringTokenizer(line);

						int _stage = Integer.parseInt(tk.nextToken());
						int _start = Integer.parseInt(tk.nextToken());
						int _end = Integer.parseInt(tk.nextToken());
						int _cost = Integer.parseInt(tk.nextToken());
						int _time = Integer.parseInt(tk.nextToken());

						schemeElement s_e = new schemeElement(_stage, _start, _end, _cost, _time);

						if(_stage == 1){
							s.firstStage.add(s_e);
						}
						else if(_stage == 2){
							s.secondStage.add(s_e);
						}
						else if(_stage == 3){
							s.thirdStage.add(s_e);
						}
						else{
							System.out.println("NoStageError in the scheme input section.");
						}

						line = br.readLine();
					}

					schemes.add(s);
				}
			}
		}catch(IOException ioe){
			ioe.printStackTrace();
		}
	}

	public static void chromosomePrinter(ArrayList<Chromosome> c_list){
		
		for(int i=0; i<c_list.size();i++){

			Chromosome c = c_list.get(i);

			System.out.println("Serial Number : "+i);

			for(int k=0;k<3;k++){

				ChromosomeScheme s0 = c.chromosomeParts.get(k);

				System.out.print("Supplier: ");

				for(int j=0; j<8;j++){
					int sum = 0; 
					sum += s0.supplierGeneValues[(j*3)+0];
					sum += s0.supplierGeneValues[(j*3)+1];
					sum += s0.supplierGeneValues[(j*3)+2];

					System.out.print(sum+",");
				}
				System.out.println();

				System.out.print("Customer: ");
				int sum =0;
				for(int j=0;j<4;j++){
					System.out.print(s0.customerGeneValues[j]+" ");
					sum+= s0.customerGeneValues[j];
				}
				System.out.print("sum: "+sum+"\n\n");

			}
		}
	}

	public static void chromosomeFitnessPrinter(ArrayList<Chromosome> c_list){
		PrintWriter pw = null;
		try{
			pw = new PrintWriter(new FileWriter("data.txt"));
		}catch(IOException ioe){
			ioe.printStackTrace();
		}
		
		for(int i=0; i<c_list.size();i++){

			if(i==200){break;}

			Chromosome c = c_list.get(i);

			double val = 20000000.0 + (-10.0 *(double)c.cost)+(-8595.0*(double)c.time)+(30.0*(double)c.quality);

			int lossval = GenAlgoObject.lossCalculator(c);

			if(i==0){
				try(FileWriter fw = new FileWriter("minitab data.txt", true);
				    BufferedWriter bw = new BufferedWriter(fw);
				    PrintWriter out = new PrintWriter(bw))
				{
					out.println("Serial: "+i+" cost: "+c.cost+" time: "+c.time+" grade: "+c.quality+" loss:"+lossval);
				    out.println("Fitness value: "+val+"\n");
				    out.close();
				} catch (IOException e) {
				    e.printStackTrace();
				}
			}

			

			if(i%5 == 0){
				System.out.println("Serial: "+i+" cost: "+c.cost+" time: "+c.time+" grade: "+c.quality+" loss:"+lossval+ " fitness value: "+val);
			}
			pw.println(c.cost+","+c.time+","+c.quality);
		}

		pw.close();


		PrintWriter pw1 = null;
		try{
			pw1 = new PrintWriter(new FileWriter("chromosome gene values.txt"));
		}catch(IOException ioe){
			ioe.printStackTrace();
		}

		for(int i=0; i<c_list.size();i++){

			if(i==200){break;}

			Chromosome c = c_list.get(i);

			pw1.println("Index: "+i);

			for(int k=0; k<c.chromosomeParts.size();k++){
				
				ChromosomeScheme cs_temp = c.chromosomeParts.get(k);

				for(int j=0; j<24; j++){
					pw1.print(cs_temp.supplierGeneValues[j]+", ");
				}
				pw1.println();
				for(int j =0; j<4; j++){
					pw1.print(cs_temp.customerGeneValues[j]+", ");
				}
				pw1.println();
			}

		}

		pw1.close();

	}

	public static void printSchemes(ArrayList<Scheme> listOfSchemes){
		for(int i = 0; i<listOfSchemes.size(); i++){
			
			Scheme s = listOfSchemes.get(i);

			System.out.println("Scheme Number: "+s.schId);

			for(int j=0; j<s.firstStage.size(); j++){
				System.out.print(s.firstStage.get(j));
			}
			System.out.println();

			for(int j=0; j<s.secondStage.size(); j++){
				System.out.print(s.secondStage.get(j));
			}
			System.out.println();

			for(int j=0; j<s.thirdStage.size(); j++){
				System.out.print(s.thirdStage.get(j));
			}
			System.out.println();
		}
	}

}

class Driver{
	public static Utilities u ;
	public static ArrayList<Supplier> s_list;
	public static ArrayList<Scheme> scheme_list;
	public static ArrayList<Integer> d_list;
	public static GenAlgoObject ga;

	public static void main(String[] args) {
		
		u = new Utilities();
		s_list = new ArrayList<Supplier>();
		scheme_list = new ArrayList<Scheme>();
		d_list = new ArrayList<Integer>();

		u.supplierInput(args[0],s_list);
		u.schemeInput(args[1],scheme_list);
		u.demandInput(args[2],d_list);

		int sumDemand = 0;
		for(int i=0;i<d_list.size();i++){
			sumDemand += d_list.get(i);
		}

		try(FileWriter fw = new FileWriter("minitab data.txt", true);
		    BufferedWriter bw = new BufferedWriter(fw);
		    PrintWriter out = new PrintWriter(bw))
		{
		    out.println("\ninitial size:"+args[3]+" generation number: "+args[4]+" Crossover: "+args[5]+" Mutation: "+args[6]);
		    out.close();
		} catch (IOException e) {
		    e.printStackTrace();
		}



		ga = new GenAlgoObject(sumDemand, s_list, scheme_list, d_list);
		
		ga.initialPopulationGeneration(Integer.parseInt(args[3]));

		u.chromosomeFitnessPrinter(ga.population);

		ga.evolutionProcess(Integer.parseInt(args[4]),Integer.parseInt(args[3]),Integer.parseInt(args[5]),Integer.parseInt(args[6]));
		
		System.out.println("\nSolution space: \n");

		u.chromosomeFitnessPrinter(ga.population);
	}
}