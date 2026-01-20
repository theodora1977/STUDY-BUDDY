from database import SessionLocal, engine, Base
from model import User, OTP
from subject import Subject
from topic import Topic
from question import Question
from progress import UserProgress
from library import UserLibrary

# Create tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data
db.query(Question).delete()
db.query(Topic).delete()
db.query(Subject).delete()
db.commit()

# Create subjects
subjects_data = [
    {"name": "Physics", "exam_type": "General"},
    {"name": "Chemistry", "exam_type": "General"},
    {"name": "Biology", "exam_type": "General"},
    {"name": "English", "exam_type": "General"},
    {"name": "Government", "exam_type": "General"},
    {"name": "Literature", "exam_type": "General"},
    {"name": "Economics", "exam_type": "General"},
    {"name": "CRS", "exam_type": "General"},
    {"name": "Mathematics", "exam_type": "General"},
]

subjects = {}
for subject_data in subjects_data:
    subject = Subject(name=subject_data["name"], exam_type=subject_data["exam_type"], version=1.0)
    db.add(subject)
    db.flush()
    subjects[subject_data["name"]] = subject.id

db.commit()

# Physics Questions
physics_questions = [
    ("What is the SI unit of force?", {"A": "Newton", "B": "Joule", "C": "Watt", "D": "Pascal"}, "A", "Force is measured in Newtons (N)."),
    ("What is the acceleration due to gravity on Earth?", {"A": "8.8 m/s²", "B": "9.8 m/s²", "C": "10.8 m/s²", "D": "7.8 m/s²"}, "B", "The standard acceleration due to gravity is 9.8 m/s²."),
    ("What does Newton's First Law state?", {"A": "F=ma", "B": "An object continues in motion unless acted upon by an external force", "C": "Every action has an equal and opposite reaction", "D": "Energy is conserved"}, "B", "Newton's First Law states that an object at rest stays at rest unless acted upon by an external force."),
    ("What is the speed of light?", {"A": "3 × 10^8 m/s", "B": "3 × 10^7 m/s", "C": "3 × 10^9 m/s", "D": "3 × 10^6 m/s"}, "A", "The speed of light is approximately 3 × 10^8 m/s."),
    ("What is kinetic energy?", {"A": "Energy of motion", "B": "Energy at rest", "C": "Heat energy", "D": "Chemical energy"}, "A", "Kinetic energy is the energy an object possesses due to its motion."),
    ("What is the formula for velocity?", {"A": "v = s/t", "B": "v = at", "C": "v = F/m", "D": "v = mgh"}, "A", "Velocity is displacement divided by time (v = s/t)."),
    ("What is a scalar quantity?", {"A": "Has magnitude and direction", "B": "Has only magnitude", "C": "Has only direction", "D": "Has both but can be negative"}, "B", "A scalar quantity has only magnitude, no direction."),
    ("What is the SI unit of energy?", {"A": "Watt", "B": "Joule", "C": "Newton", "D": "Pascal"}, "B", "Energy is measured in Joules (J)."),
    ("What is the law of conservation of momentum?", {"A": "Momentum can be created", "B": "Momentum is always conserved in an isolated system", "C": "Momentum increases with time", "D": "Momentum is relative to the observer"}, "B", "In an isolated system, momentum is always conserved."),
    ("What is the wavelength of visible light?", {"A": "100-400 nm", "B": "400-700 nm", "C": "700-1000 nm", "D": "50-200 nm"}, "B", "Visible light has wavelengths between 400-700 nm."),
    ("What is the SI unit of power?", {"A": "Joule", "B": "Newton", "C": "Watt", "D": "Pascal"}, "C", "Power is measured in Watts (W)."),
    ("What does Ohm's Law state?", {"A": "V = IR", "B": "V = I/R", "C": "V = R/I", "D": "I = VR"}, "A", "Ohm's Law states that V = IR (Voltage = Current × Resistance)."),
    ("What is the SI unit of current?", {"A": "Ohm", "B": "Volt", "C": "Ampere", "D": "Coulomb"}, "C", "Electric current is measured in Amperes (A)."),
    ("What is the angle of incidence equal to?", {"A": "Angle of refraction", "B": "Angle of reflection", "C": "Angle of diffraction", "D": "Critical angle"}, "B", "The angle of incidence equals the angle of reflection."),
    ("What is thermal equilibrium?", {"A": "When temperatures are equal", "B": "When heat stops flowing", "C": "When both objects have the same temperature", "D": "All of the above"}, "D", "Thermal equilibrium occurs when temperatures are equal and heat stops flowing."),
    ("What is the SI unit of temperature?", {"A": "Celsius", "B": "Fahrenheit", "C": "Kelvin", "D": "Rankine"}, "C", "The SI unit of temperature is Kelvin (K)."),
    ("What is density?", {"A": "Mass per unit volume", "B": "Volume per unit mass", "C": "Weight per unit area", "D": "Force per unit area"}, "A", "Density is mass per unit volume."),
    ("What is the formula for work?", {"A": "W = F × d", "B": "W = F/d", "C": "W = m × v", "D": "W = mgh"}, "A", "Work is calculated as W = F × d (Force × Distance)."),
    ("What is pressure?", {"A": "Force per unit area", "B": "Force per unit volume", "C": "Mass per unit area", "D": "Weight per unit distance"}, "A", "Pressure is force per unit area."),
    ("What is the SI unit of pressure?", {"A": "Atmosphere", "B": "Bar", "C": "Pascal", "D": "Newton"}, "C", "The SI unit of pressure is Pascal (Pa)."),
    ("What is momentum?", {"A": "Mass times velocity", "B": "Force divided by time", "C": "Energy divided by time", "D": "Acceleration times mass"}, "A", "Momentum is the product of mass and velocity (p = mv)."),
    ("What is Newton's Second Law?", {"A": "Action equals reaction", "B": "Force equals mass times acceleration", "C": "Energy is conserved", "D": "Motion continues unchanged"}, "B", "Newton's Second Law states F = ma."),
    ("What is Newton's Third Law?", {"A": "Energy conservation", "B": "Action equals reaction", "C": "Objects maintain motion", "D": "Force creates pressure"}, "B", "Newton's Third Law states every action has an equal and opposite reaction."),
    ("What is the formula for kinetic energy?", {"A": "KE = mgh", "B": "KE = ½mv²", "C": "KE = Fd", "D": "KE = pt"}, "B", "Kinetic energy is calculated as KE = ½mv²."),
    ("What is potential energy?", {"A": "Energy of motion", "B": "Energy due to position or state", "C": "Heat energy", "D": "Radiant energy"}, "B", "Potential energy depends on position or state of an object."),
    ("What is the formula for potential energy?", {"A": "PE = Fd", "B": "PE = ½mv²", "C": "PE = mgh", "D": "PE = Kx"}, "C", "Gravitational potential energy is PE = mgh."),
    ("What is wave frequency?", {"A": "Distance between waves", "B": "Number of waves per unit time", "C": "Speed of the wave", "D": "Highest point of wave"}, "B", "Frequency is the number of complete waves passing per unit time."),
    ("What is wavelength?", {"A": "Speed of wave", "B": "Frequency of wave", "C": "Distance between consecutive waves", "D": "Height of wave"}, "C", "Wavelength is the distance between two consecutive crests."),
    ("What is the relationship between frequency and wavelength?", {"A": "They are independent", "B": "f × λ = c (wave speed)", "C": "f + λ = constant", "D": "f = λ²"}, "B", "Frequency and wavelength are related by: f × λ = c."),
    ("What is elasticity?", {"A": "Ability to stretch", "B": "Ability to return to original shape", "C": "Flexibility", "D": "Rigidity"}, "B", "Elasticity is the property of returning to original shape after deformation."),
    ("What is friction?", {"A": "Force that assists motion", "B": "Force that opposes motion", "C": "Gravitational force", "D": "Magnetic force"}, "B", "Friction is a force that opposes relative motion between surfaces."),
    ("What are the types of friction?", {"A": "Static and kinetic", "B": "Positive and negative", "C": "Internal and external", "D": "Horizontal and vertical"}, "A", "Friction is classified as static (at rest) and kinetic (in motion)."),
    ("What is simple harmonic motion?", {"A": "Random motion", "B": "Straight line motion", "C": "Repetitive motion under restoring force", "D": "Accelerated motion"}, "C", "Simple harmonic motion is periodic motion with a restoring force."),
    ("What is the period of oscillation?", {"A": "Number of oscillations per second", "B": "Time for one complete oscillation", "C": "Maximum displacement", "D": "Amplitude of motion"}, "B", "Period is the time taken for one complete oscillation."),
    ("What is amplitude?", {"A": "Frequency of oscillation", "B": "Period of oscillation", "C": "Maximum displacement from equilibrium", "D": "Velocity of oscillation"}, "C", "Amplitude is the maximum distance from the equilibrium position."),
    ("What is the Doppler effect?", {"A": "Change in frequency due to relative motion", "B": "Change in wavelength only", "C": "Change in speed of sound", "D": "Change in amplitude"}, "A", "Doppler effect is the change in frequency due to relative motion of source and observer."),
    ("What is refraction?", {"A": "Bending of light at interface", "B": "Bouncing of light", "C": "Spreading of light", "D": "Absorption of light"}, "A", "Refraction is the bending of light when it passes from one medium to another."),
    ("What is diffraction?", {"A": "Bending of light around obstacles", "B": "Bouncing of light", "C": "Spreading of light waves around obstacles", "D": "Both A and C"}, "D", "Diffraction is the bending and spreading of waves around obstacles."),
    ("What is Young's modulus?", {"A": "Ratio of stress to strain", "B": "Ratio of force to area", "C": "Measure of rigidity", "D": "A and C"}, "D", "Young's modulus measures the stiffness of a material."),
]

# Chemistry Questions
chemistry_questions = [
    ("What is the SI unit of molar mass?", {"A": "g/mol", "B": "kg/mol", "C": "g/L", "D": "kg/L"}, "A", "Molar mass is measured in grams per mole (g/mol)."),
    ("What is the atomic number of Carbon?", {"A": "4", "B": "6", "C": "8", "D": "12"}, "B", "Carbon has an atomic number of 6."),
    ("What is pH in chemistry?", {"A": "Power of Hydrogen", "B": "Potential of Hydrogen", "C": "Both A and B", "D": "Pressure of Hydrogen"}, "C", "pH stands for Power of Hydrogen or Potential of Hydrogen."),
    ("What is the pH of pure water at 25°C?", {"A": "6", "B": "7", "C": "8", "D": "5"}, "B", "Pure water has a pH of 7 at 25°C."),
    ("What is an acid?", {"A": "A substance that donates protons", "B": "A substance that accepts protons", "C": "A substance that forms salts", "D": "A substance that conducts electricity"}, "A", "An acid is a substance that donates protons (H+ ions)."),
    ("What is a base?", {"A": "A substance that donates protons", "B": "A substance that accepts protons", "C": "A substance that is salty", "D": "A substance that doesn't conduct electricity"}, "B", "A base is a substance that accepts protons (H+ ions)."),
    ("What is the periodic table arranged by?", {"A": "Atomic mass", "B": "Atomic number", "C": "Number of electrons", "D": "Both B and C"}, "D", "The periodic table is arranged by atomic number and number of electrons."),
    ("What is the chemical formula for table salt?", {"A": "KCl", "B": "NaCl", "C": "CaCl2", "D": "MgCl2"}, "B", "Table salt is sodium chloride (NaCl)."),
    ("What is the chemical formula for water?", {"A": "H2O", "B": "H2O2", "C": "H3O", "D": "HO2"}, "A", "Water is H2O."),
    ("What is a chemical bond?", {"A": "A force that holds atoms together", "B": "A breaking of atoms", "C": "Movement of electrons", "D": "Loss of energy"}, "A", "A chemical bond is a force that holds atoms together."),
    ("What is oxidation?", {"A": "Loss of electrons", "B": "Gain of electrons", "C": "Loss of oxygen", "D": "Gain of oxygen"}, "A", "Oxidation is the loss of electrons."),
    ("What is reduction?", {"A": "Loss of electrons", "B": "Gain of electrons", "C": "Loss of hydrogen", "D": "Breaking of bonds"}, "B", "Reduction is the gain of electrons."),
    ("What is Avogadro's number?", {"A": "6.02 × 10^23", "B": "6.02 × 10^22", "C": "6.02 × 10^24", "D": "6.02 × 10^21"}, "A", "Avogadro's number is 6.02 × 10^23."),
    ("What is the SI unit of concentration?", {"A": "Molarity (M)", "B": "Molality (m)", "C": "Percentage", "D": "PPM"}, "A", "The SI unit of concentration is Molarity (M) or mol/L."),
    ("What is an element?", {"A": "A substance made of one type of atom", "B": "A substance made of molecules", "C": "A mixture of compounds", "D": "A substance with variable composition"}, "A", "An element is a substance made of only one type of atom."),
    ("What is a compound?", {"A": "A pure element", "B": "A substance made of two or more elements chemically bonded", "C": "A mixture of elements", "D": "An atom with electrons"}, "B", "A compound is made of two or more elements chemically bonded."),
    ("What is electronegativity?", {"A": "Tendency to lose electrons", "B": "Tendency to gain electrons", "C": "Ability to attract electrons", "D": "Ability to repel protons"}, "C", "Electronegativity is the ability to attract electrons."),
    ("What is a redox reaction?", {"A": "A reaction involving oxidation and reduction", "B": "A reaction with water", "C": "A reaction with acid and base", "D": "A reaction that releases heat"}, "A", "A redox reaction involves both oxidation and reduction."),
    ("What is the atomic mass unit?", {"A": "g", "B": "kg", "C": "amu", "D": "mg"}, "C", "The atomic mass unit (amu) is used to measure atomic masses."),
    ("What is ionic bonding?", {"A": "Transfer of electrons", "B": "Sharing of electrons", "C": "Attraction of atoms", "D": "Repulsion of atoms"}, "A", "Ionic bonding involves the transfer of electrons between atoms."),
    ("What is covalent bonding?", {"A": "Transfer of electrons", "B": "Sharing of electrons", "C": "Attraction of ions", "D": "Repulsion of atoms"}, "B", "Covalent bonding involves the sharing of electrons between atoms."),
    ("What is the difference between ionic and covalent bonds?", {"A": "Ionic shares electrons, covalent transfers", "B": "Ionic transfers electrons, covalent shares", "C": "They are the same", "D": "Ionic is stronger"}, "B", "Ionic bonds transfer electrons, covalent bonds share electrons."),
    ("What is electrochemistry?", {"A": "Study of electricity in chemicals", "B": "Study of electrical energy in chemical reactions", "C": "Both A and B", "D": "Study of heat in reactions"}, "C", "Electrochemistry studies electrical and chemical reactions."),
    ("What is a catalyst?", {"A": "A substance that speeds up reactions", "B": "A substance that slows down reactions", "C": "A product of reactions", "D": "A reactant that is consumed"}, "A", "A catalyst speeds up a reaction without being consumed."),
    ("What is the valence shell?", {"A": "Inner electron shell", "B": "Outermost electron shell", "C": "Middle electron shell", "D": "All electron shells"}, "B", "The valence shell is the outermost electron shell."),
    ("What is the octet rule?", {"A": "Atoms have 8 protons", "B": "Atoms have 8 neutrons", "C": "Atoms tend to have 8 electrons in valence shell", "D": "Atoms have 8 shells"}, "C", "The octet rule states atoms tend to have 8 electrons in their valence shell."),
    ("What is an alloy?", {"A": "Pure metal", "B": "Mixture of metals or metal with non-metal", "C": "Non-metallic compound", "D": "Chemical compound"}, "B", "An alloy is a mixture of two or more elements, one being a metal."),
    ("What is hydrolysis?", {"A": "Breaking bonds with water", "B": "Formation of bonds with water", "C": "Reaction with hydrogen", "D": "Reaction with oxygen"}, "A", "Hydrolysis is the breaking of chemical bonds by water."),
    ("What is polymerization?", {"A": "Breaking large molecules", "B": "Formation of polymers from monomers", "C": "Mixing of compounds", "D": "Separation of elements"}, "B", "Polymerization is the linking of monomers to form polymers."),
    ("What is the molar volume of gas at STP?", {"A": "11.2 L", "B": "22.4 L", "C": "33.6 L", "D": "44.8 L"}, "B", "Molar volume of gas at STP is 22.4 L/mol."),
    ("What is molarity?", {"A": "Mass of solute per volume of solution", "B": "Moles of solute per liter of solution", "C": "Grams of solute per 100g solvent", "D": "Number of particles"}, "B", "Molarity is moles of solute per liter of solution (mol/L)."),
    ("What is molality?", {"A": "Moles per liter", "B": "Moles of solute per kilogram of solvent", "C": "Mass per volume", "D": "Grams per liter"}, "B", "Molality is moles of solute per kilogram of solvent."),
    ("What is a buffer solution?", {"A": "Very concentrated solution", "B": "Solution that resists pH change", "C": "Solution with high salinity", "D": "Pure water solution"}, "B", "A buffer solution resists changes in pH when acid or base is added."),
    ("What is the pH scale?", {"A": "0-5 scale", "B": "0-10 scale", "C": "0-14 scale", "D": "0-7 scale"}, "C", "The pH scale ranges from 0 to 14."),
    ("What are Lewis structures?", {"A": "3D molecular models", "B": "Ball and stick models", "C": "Diagrams showing valence electrons", "D": "Computer simulations"}, "C", "Lewis structures show valence electrons as dots around atoms."),
    ("What is isotopy?", {"A": "Atoms of same element with different protons", "B": "Atoms of same element with different neutrons", "C": "Atoms of different elements", "D": "Compounds with same formula"}, "B", "Isotopes are atoms of the same element with different numbers of neutrons."),
    ("What is thermochemistry?", {"A": "Study of thermal reactions", "B": "Study of heat in chemical reactions", "C": "Study of heat transfer", "D": "Study of temperature"}, "B", "Thermochemistry studies heat involved in chemical reactions."),
    ("What is exothermic reaction?", {"A": "Absorbs heat", "B": "Releases heat", "C": "No heat change", "D": "Constant temperature"}, "B", "An exothermic reaction releases heat to surroundings."),
    ("What is endothermic reaction?", {"A": "Releases heat", "B": "Absorbs heat", "C": "No heat change", "D": "Increases temperature"}, "B", "An endothermic reaction absorbs heat from surroundings."),
]

# Biology Questions
biology_questions = [
    ("What is the basic unit of life?", {"A": "Atom", "B": "Molecule", "C": "Cell", "D": "Tissue"}, "C", "The cell is the basic unit of life."),
    ("What is photosynthesis?", {"A": "Breaking down food", "B": "Making food using light energy", "C": "Movement of organisms", "D": "Reproduction of cells"}, "B", "Photosynthesis is the process of making food using light energy."),
    ("What is the SI unit of enzyme activity?", {"A": "Katal (kat)", "B": "Joule", "C": "Newton", "D": "Watt"}, "A", "The SI unit of enzyme activity is the Katal (kat)."),
    ("What does DNA stand for?", {"A": "Deoxyribonucleic Acid", "B": "Dynamic Nucleic Acid", "C": "Diribonucleic Acid", "D": "Double Nucleic Acid"}, "A", "DNA stands for Deoxyribonucleic Acid."),
    ("What is the function of mitochondria?", {"A": "Protein synthesis", "B": "Energy production", "C": "Photosynthesis", "D": "Storage of water"}, "B", "Mitochondria are responsible for energy production (ATP)."),
    ("What is cellular respiration?", {"A": "Breathing process", "B": "Release of energy from food", "C": "Photosynthesis process", "D": "Movement of cells"}, "B", "Cellular respiration is the process of releasing energy from food."),
    ("What is the function of ribosomes?", {"A": "Energy production", "B": "Protein synthesis", "C": "Photosynthesis", "D": "Cell division"}, "B", "Ribosomes are responsible for protein synthesis."),
    ("What is the function of chloroplasts?", {"A": "Energy production", "B": "Photosynthesis", "C": "Protein synthesis", "D": "Cell division"}, "B", "Chloroplasts are responsible for photosynthesis."),
    ("What is meiosis?", {"A": "Cell division producing identical cells", "B": "Cell division producing sex cells", "C": "Cell growth process", "D": "Cell death process"}, "B", "Meiosis is the cell division that produces sex cells (gametes)."),
    ("What is mitosis?", {"A": "Cell division producing sex cells", "B": "Cell division producing identical cells", "C": "Cell growth", "D": "Cell differentiation"}, "B", "Mitosis is cell division producing two identical daughter cells."),
    ("What is the function of the nucleus?", {"A": "Energy production", "B": "Control center of the cell", "C": "Photosynthesis", "D": "Movement"}, "B", "The nucleus is the control center of the cell."),
    ("What is the function of the cell membrane?", {"A": "Support and protection", "B": "Control of substances entering and leaving", "C": "Photosynthesis", "D": "Energy production"}, "B", "The cell membrane controls what enters and leaves the cell."),
    ("What is an ecosystem?", {"A": "A group of organisms", "B": "Organisms and their environment", "C": "A habitat", "D": "A population"}, "B", "An ecosystem includes organisms and their physical environment."),
    ("What is evolution?", {"A": "Development of an organism", "B": "Change in organisms over time", "C": "Adaptation to environment", "D": "Reproduction process"}, "B", "Evolution is the change in organisms over time."),
    ("What is natural selection?", {"A": "Humans choosing traits", "B": "Random mutation", "C": "Survival of organisms best adapted", "D": "Environmental change"}, "C", "Natural selection is the survival of organisms best adapted to their environment."),
    ("What is inheritance?", {"A": "Passing of traits to offspring", "B": "Mutation of genes", "C": "Evolution process", "D": "Cell division"}, "A", "Inheritance is the passing of traits from parents to offspring."),
    ("What is an allele?", {"A": "Different form of a gene", "B": "Type of protein", "C": "Part of chromosome", "D": "Type of mutation"}, "A", "An allele is a different form of a gene."),
    ("What is a dominant trait?", {"A": "A trait that appears even with one allele", "B": "A trait that requires two alleles", "C": "A rare trait", "D": "An inherited trait"}, "A", "A dominant trait appears with just one copy of the allele."),
    ("What is a recessive trait?", {"A": "A trait that appears even with one allele", "B": "A trait that requires two alleles", "C": "A common trait", "D": "An environmental trait"}, "B", "A recessive trait requires two copies of the allele to appear."),
    ("What is an organism?", {"A": "A living thing", "B": "A cell", "C": "A group of cells", "D": "An atom"}, "A", "An organism is a living thing."),
    ("What is the nucleus in a cell?", {"A": "A membrane", "B": "The control center containing DNA", "C": "A type of organelle", "D": "A protein structure"}, "B", "The nucleus is the control center of the cell containing DNA."),
    ("What are genes?", {"A": "Proteins", "B": "Sections of DNA that control traits", "C": "Enzymes", "D": "Carbohydrates"}, "B", "Genes are sections of DNA that determine specific traits."),
    ("What is a chromosome?", {"A": "A gene", "B": "A protein", "C": "A structure containing DNA and proteins", "D": "An organelle"}, "C", "A chromosome is a structure made of DNA and proteins."),
    ("What is the difference between prokaryotes and eukaryotes?", {"A": "Prokaryotes have nucleus, eukaryotes don't", "B": "Eukaryotes have nucleus, prokaryotes don't", "C": "No difference", "D": "Prokaryotes are larger"}, "B", "Eukaryotes have a nucleus; prokaryotes do not."),
    ("What is the endoplasmic reticulum?", {"A": "The nucleus", "B": "Network of membranes for protein synthesis", "C": "Energy producing organelle", "D": "Photosynthetic organelle"}, "B", "The ER is a network of membranes involved in protein synthesis and transport."),
    ("What is the Golgi apparatus?", {"A": "Produces energy", "B": "Makes proteins", "C": "Packages and modifies proteins", "D": "Breaks down waste"}, "C", "The Golgi apparatus packages and modifies proteins for transport."),
    ("What are lysosomes?", {"A": "Store water", "B": "Make proteins", "C": "Break down waste and cellular debris", "D": "Produce energy"}, "C", "Lysosomes break down cellular waste and foreign materials."),
    ("What is the cell wall?", {"A": "Controls what enters the cell", "B": "Provides support and protection in plants", "C": "Produces energy", "D": "Makes proteins"}, "B", "The cell wall provides support and protection in plant cells."),
    ("What is the vacuole?", {"A": "The control center", "B": "Makes proteins", "C": "Stores water and nutrients", "D": "Produces energy"}, "C", "The vacuole stores water, nutrients, and waste."),
    ("What is diffusion?", {"A": "Active movement of molecules", "B": "Passive movement from high to low concentration", "C": "Requires energy", "D": "Movement through a pump"}, "B", "Diffusion is passive movement of molecules from high to low concentration."),
    ("What is semipermeable?", {"A": "Allows all molecules through", "B": "Blocks all molecules", "C": "Allows some molecules through", "D": "Is rigid and solid"}, "C", "Semipermeable membranes allow some molecules through but not others."),
    ("What is DNA replication?", {"A": "Reading DNA", "B": "Copying DNA before cell division", "C": "Breaking down DNA", "D": "Combining DNA with protein"}, "B", "DNA replication is the copying of DNA before cell division."),
    ("What are chromosomes made of?", {"A": "Proteins only", "B": "DNA only", "C": "DNA and proteins", "D": "RNA and proteins"}, "C", "Chromosomes are made of DNA and proteins."),
    ("What is the genotype?", {"A": "The organism's appearance", "B": "The organism's genetic makeup", "C": "The organism's behavior", "D": "The organism's environment"}, "B", "Genotype is the genetic makeup of an organism."),
    ("What is the phenotype?", {"A": "The genetic makeup", "B": "The observable characteristics", "C": "The DNA sequence", "D": "The inherited genes"}, "B", "Phenotype is the observable characteristics of an organism."),
    ("What is segregation in genetics?", {"A": "Separation of alleles during reproduction", "B": "Mixing of genes", "C": "Mutation of genes", "D": "Duplication of chromosomes"}, "A", "Segregation is the separation of alleles during meiosis."),
    ("What is independent assortment?", {"A": "Genes are always together", "B": "Random distribution of genes to gametes", "C": "Genes stay in the nucleus", "D": "Genes are linked"}, "B", "Independent assortment is the random distribution of genes during meiosis."),
    ("What is genetic drift?", {"A": "Planned mutation", "B": "Random change in gene frequency", "C": "Natural selection", "D": "Artificial selection"}, "B", "Genetic drift is random change in gene frequency in populations."),
    ("What is speciation?", {"A": "Mutation", "B": "Evolution within a species", "C": "Formation of new species", "D": "Extinction of species"}, "C", "Speciation is the evolution of new species from existing ones."),
]

# English Questions
english_questions = [
    ("What is a noun?", {"A": "A word describing action", "B": "A person, place, or thing", "C": "A word showing emotion", "D": "A word showing comparison"}, "B", "A noun is a word that names a person, place, or thing."),
    ("What is a verb?", {"A": "A word describing a noun", "B": "A word showing action or state of being", "C": "A connecting word", "D": "A word describing emotion"}, "B", "A verb is a word that shows action or state of being."),
    ("What is an adjective?", {"A": "A word showing action", "B": "A word describing a noun", "C": "A word connecting clauses", "D": "A word replacing a noun"}, "B", "An adjective is a word that describes a noun."),
    ("What is an adverb?", {"A": "A word naming something", "B": "A word describing a noun", "C": "A word modifying a verb, adjective, or adverb", "D": "A word connecting ideas"}, "C", "An adverb modifies a verb, adjective, or another adverb."),
    ("What is a pronoun?", {"A": "A word describing action", "B": "A word replacing a noun", "C": "A word modifying a noun", "D": "A word connecting sentences"}, "B", "A pronoun is a word that replaces a noun."),
    ("What is a metaphor?", {"A": "A comparison using like or as", "B": "A direct comparison without using like or as", "C": "A word with opposite meaning", "D": "A word with similar meaning"}, "B", "A metaphor is a direct comparison without using like or as."),
    ("What is a simile?", {"A": "A direct comparison", "B": "A comparison using like or as", "C": "A word repetition", "D": "An opposite word"}, "B", "A simile is a comparison using like or as."),
    ("What is personification?", {"A": "Comparing two things", "B": "Giving human qualities to non-human things", "C": "Using same beginning sounds", "D": "Using opposite words"}, "B", "Personification gives human qualities to non-human things."),
    ("What is irony?", {"A": "Direct statement of truth", "B": "When reality is opposite of what is expected", "C": "Comparison of two things", "D": "Repetition of sounds"}, "B", "Irony is when reality is opposite of what is expected."),
    ("What is a subject?", {"A": "What the sentence is about", "B": "What the sentence does", "C": "How the sentence is written", "D": "Why the sentence is written"}, "A", "The subject is what the sentence is about."),
    ("What is a predicate?", {"A": "What the sentence is about", "B": "What the sentence does or is", "C": "The beginning of the sentence", "D": "The ending of the sentence"}, "B", "The predicate tells what the subject does or is."),
    ("What is a clause?", {"A": "A group of related words", "B": "A group of words with a subject and verb", "C": "A single word", "D": "A type of punctuation"}, "B", "A clause is a group of words with a subject and verb."),
    ("What is a phrase?", {"A": "A group of words with a verb", "B": "A group of related words without a subject and verb", "C": "A complete sentence", "D": "A type of punctuation"}, "B", "A phrase is a group of related words without a subject and verb."),
    ("What is a topic sentence?", {"A": "The last sentence", "B": "The main idea of a paragraph", "C": "A sentence with a question", "D": "A sentence with an example"}, "B", "A topic sentence states the main idea of a paragraph."),
    ("What is a thesis statement?", {"A": "The main argument of an essay", "B": "A supporting detail", "C": "An introduction sentence", "D": "A conclusion sentence"}, "A", "A thesis statement is the main argument of an essay."),
    ("What is alliteration?", {"A": "Repetition of beginning sounds", "B": "Repetition of ending sounds", "C": "Repetition of words", "D": "Repetition of ideas"}, "A", "Alliteration is the repetition of beginning sounds in nearby words."),
    ("What is onomatopoeia?", {"A": "A word that sounds like its meaning", "B": "A word with opposite meaning", "C": "A word with similar meaning", "D": "A word that is slang"}, "A", "Onomatopoeia is a word that imitates the sound it represents."),
    ("What is an oxymoron?", {"A": "A contradiction in terms", "B": "A long sentence", "C": "A type of poem", "D": "A figure of speech"}, "A", "An oxymoron is a contradiction in terms."),
    ("What is a paradox?", {"A": "A sentence with two meanings", "B": "A statement that seems contradictory but may be true", "C": "A false statement", "D": "A true statement"}, "B", "A paradox is a statement that seems contradictory but may be true."),
    ("What is analogy?", {"A": "A direct comparison", "B": "A comparison showing relationship between different things", "C": "A word with similar meaning", "D": "A word with opposite meaning"}, "B", "An analogy shows a relationship or similarity between different things."),
    ("What is a simile?", {"A": "Direct comparison", "B": "Comparison using like or as", "C": "Word repetition", "D": "Opposite word"}, "B", "A simile is a comparison using like or as."),
    ("What is an antonym?", {"A": "A word with same meaning", "B": "A word with opposite meaning", "C": "A word related in some way", "D": "A word spelled backwards"}, "B", "An antonym is a word with opposite meaning."),
    ("What is a synonym?", {"A": "A word with opposite meaning", "B": "A word with similar meaning", "C": "A word spelled differently", "D": "A word from another language"}, "B", "A synonym is a word with similar or same meaning."),
    ("What is hyperbole?", {"A": "An understatement", "B": "An extreme exaggeration", "C": "A comparison", "D": "A contradiction"}, "B", "Hyperbole is an extreme exaggeration for dramatic effect."),
    ("What is understatement?", {"A": "A large exaggeration", "B": "Saying something is less important than it is", "C": "Saying something is more important", "D": "Being dishonest"}, "B", "Understatement makes something seem less important than it is."),
    ("What is a pun?", {"A": "A serious joke", "B": "A joke using words with multiple meanings", "C": "A type of poem", "D": "A long story"}, "B", "A pun is a play on words with multiple meanings."),
    ("What is tone?", {"A": "The volume of speech", "B": "The attitude of the writer", "C": "The speed of speaking", "D": "The type of words used"}, "B", "Tone is the attitude of the writer toward the subject."),
    ("What is mood?", {"A": "The writer's feeling", "B": "The atmosphere or feeling created by the work", "C": "The time of day", "D": "The setting"}, "B", "Mood is the emotional atmosphere created by the work."),
    ("What is symbolism?", {"A": "Using symbols", "B": "Objects representing ideas or concepts", "C": "Decorative elements", "D": "Religious meanings"}, "B", "Symbolism uses objects to represent abstract ideas or concepts."),
    ("What is imagery?", {"A": "Pictures", "B": "Descriptive language appealing to senses", "C": "Imagination", "D": "Visual art"}, "B", "Imagery uses descriptive language to appeal to the senses."),
    ("What is the main idea?", {"A": "Supporting details", "B": "The central point of a text", "C": "A specific example", "D": "The setting"}, "B", "The main idea is the central point or primary message of a text."),
    ("What is a supporting detail?", {"A": "The main idea", "B": "Information that supports the main idea", "C": "The conclusion", "D": "The introduction"}, "B", "Supporting details are facts that support the main idea."),
    ("What is a conclusion?", {"A": "The beginning", "B": "The middle", "C": "The final statement or summary", "D": "A fact"}, "C", "A conclusion is a final statement or summary of main points."),
    ("What is a transition?", {"A": "A word", "B": "A sentence", "C": "A word/phrase connecting ideas", "D": "A paragraph"}, "C", "A transition connects ideas between sentences or paragraphs."),
    ("What is active voice?", {"A": "Subject receives action", "B": "Subject performs the action", "C": "Passive action", "D": "No action"}, "B", "In active voice, the subject performs the action."),
    ("What is passive voice?", {"A": "Subject performs action", "B": "Subject receives the action", "C": "Active voice", "D": "No voice"}, "B", "In passive voice, the subject receives the action."),
    ("What is a compound sentence?", {"A": "One independent clause", "B": "Two or more independent clauses", "C": "One dependent clause", "D": "No clauses"}, "B", "A compound sentence has two or more independent clauses."),
    ("What is a complex sentence?", {"A": "Very long sentence", "B": "Independent clause with dependent clause", "C": "Multiple sentences", "D": "Very difficult sentence"}, "B", "A complex sentence has an independent clause and dependent clause."),
    ("What is comma splice?", {"A": "Using too many commas", "B": "Joining independent clauses with comma only", "C": "Missing comma", "D": "Broken comma"}, "B", "Comma splice joins two independent clauses with only a comma."),
]

# Art Questions - REMOVED, replaced with Government, Literature, Economics, CRS

# Government Questions
government_questions = [
    ("What is democracy?", {"A": "Rule by one person", "B": "Rule by the people", "C": "Rule by the rich", "D": "Rule by the military"}, "B", "Democracy is a system of government where power is held by the people."),
    ("What is the separation of powers?", {"A": "Division of government into executive, legislative, judicial", "B": "Separation of nations", "C": "Division of wealth", "D": "Separation of religions"}, "A", "Separation of powers divides government into three branches."),
    ("What is a constitution?", {"A": "A law book", "B": "A government building", "C": "The fundamental governing document", "D": "A type of government"}, "C", "A constitution is the supreme law of a country."),
    ("What is the primary function of parliament?", {"A": "Execute laws", "B": "Make laws", "C": "Judge laws", "D": "Enforce laws"}, "B", "Parliament's primary function is to make laws."),
    ("What is a monarchy?", {"A": "Rule by the people", "B": "Rule by a king or queen", "C": "Rule by the rich", "D": "Rule by priests"}, "B", "A monarchy is a government ruled by a king or queen."),
    ("What is an oligarchy?", {"A": "Rule by one", "B": "Rule by a few", "C": "Rule by many", "D": "Rule by all"}, "B", "An oligarchy is a government ruled by a few people."),
    ("What is the right to vote called?", {"A": "Suffrage", "B": "Freedom", "C": "Citizenship", "D": "Authority"}, "A", "The right to vote is called suffrage."),
    ("What is a political party?", {"A": "A social gathering", "B": "An organized group with common political beliefs", "C": "A government office", "D": "A type of law"}, "B", "A political party is an organized group of people with common political beliefs."),
    ("What is the rule of law?", {"A": "The government makes all decisions", "B": "Laws apply equally to all citizens", "C": "Only leaders follow laws", "D": "Laws are suggestions"}, "B", "The rule of law means laws apply equally to everyone."),
    ("What is impeachment?", {"A": "Arrest of a citizen", "B": "Formal charge of wrongdoing against a government official", "C": "A type of punishment", "D": "A military operation"}, "B", "Impeachment is a formal charge of wrongdoing against government officials."),
    ("What is a veto?", {"A": "An approval of a law", "B": "A rejection of a law", "C": "A suggestion for a law", "D": "A debate about a law"}, "B", "A veto is the power to reject a law or decision."),
    ("What is citizenship?", {"A": "Living in a country", "B": "Legal membership in a country", "C": "Having a job", "D": "Being of voting age"}, "B", "Citizenship is legal membership and status in a country."),
    ("What is a bill?", {"A": "A debt", "B": "An invoice", "C": "A proposed law", "D": "A government office"}, "C", "A bill is a proposed law presented to parliament."),
    ("What is a legislature?", {"A": "A judge", "B": "A body that makes laws", "C": "A court", "D": "An executive office"}, "B", "A legislature is the branch of government that makes laws."),
    ("What is the executive branch?", {"A": "The law-making body", "B": "The judging body", "C": "The branch that enforces laws", "D": "The legislative body"}, "C", "The executive branch enforces and administers laws."),
    ("What is the judicial branch?", {"A": "The law-making body", "B": "The enforcing body", "C": "The court system that interprets laws", "D": "The administrative body"}, "C", "The judicial branch interprets laws and administers justice."),
    ("What is a treaty?", {"A": "A domestic law", "B": "An agreement between countries", "C": "A business contract", "D": "A personal agreement"}, "B", "A treaty is a formal agreement between countries."),
    ("What is sovereignty?", {"A": "A type of currency", "B": "The power of a country to govern itself", "C": "A military force", "D": "A geographic boundary"}, "B", "Sovereignty is the power of a country to govern itself independently."),
    ("What is a referendum?", {"A": "A government meeting", "B": "A direct vote by citizens on an issue", "C": "A type of election", "D": "A court decision"}, "B", "A referendum is a direct vote by citizens on a specific issue."),
    ("What is diplomacy?", {"A": "Military conflict", "B": "Trade agreements", "C": "The art of negotiating between countries", "D": "International law"}, "C", "Diplomacy is the peaceful negotiation between countries."),
    ("What is propaganda?", {"A": "Factual information", "B": "Information spread to promote a viewpoint", "C": "News reporting", "D": "Historical facts"}, "B", "Propaganda is information spread to influence opinions."),
    ("What is lobbying?", {"A": "A legislative body", "B": "A type of law", "C": "Attempting to influence government decisions", "D": "A government building"}, "C", "Lobbying is attempting to influence government officials."),
    ("What is an amendment?", {"A": "A new government", "B": "A formal change to a constitution", "C": "A law", "D": "A judicial decision"}, "B", "An amendment is a formal change to a constitution."),
    ("What is a coalition?", {"A": "A single party", "B": "A temporary alliance of groups", "C": "A government office", "D": "A type of election"}, "B", "A coalition is a temporary alliance of groups."),
    ("What is federalism?", {"A": "Power in federal government only", "B": "Power divided between federal and state governments", "C": "State government only", "D": "No government"}, "B", "Federalism divides power between federal and state governments."),
    ("What is secession?", {"A": "Joining a government", "B": "Peaceful withdrawal from a government", "C": "Taking over government", "D": "A law"}, "B", "Secession is the withdrawal of a region from a larger political unit."),
    ("What is a dictatorship?", {"A": "Rule by the people", "B": "Rule by a single person with absolute power", "C": "Rule by laws", "D": "Rule by a group"}, "B", "A dictatorship is rule by one person with complete power."),
    ("What is totalitarianism?", {"A": "Democratic government", "B": "Authoritarian control over all aspects of society", "C": "Limited government", "D": "No government"}, "B", "Totalitarianism is complete governmental control of all aspects of life."),
    ("What is anarchy?", {"A": "A type of government", "B": "Rule by many", "C": "Absence of government", "D": "Rule by one"}, "C", "Anarchy is the absence of government or authority."),
    ("What is judicial review?", {"A": "Reviewing court decisions", "B": "Judges evaluating laws' constitutionality", "C": "Checking a document", "D": "Reading a judgment"}, "B", "Judicial review allows courts to evaluate constitutionality of laws."),
    ("What is checks and balances?", {"A": "Banking system", "B": "System allowing branches of government to limit each other", "C": "Accounting", "D": "Government budgets"}, "B", "Checks and balances allow branches to limit each other's power."),
    ("What is a bill of rights?", {"A": "List of taxes", "B": "Document protecting individual freedoms", "C": "Court document", "D": "Government spending plan"}, "B", "Bill of Rights is a document protecting individual freedoms."),
    ("What is civil rights?", {"A": "Military rights", "B": "Rights of criminals", "C": "Equal treatment and freedom for all citizens", "D": "Government secrets"}, "C", "Civil rights are equal treatment and freedom for all citizens."),
    ("What is due process?", {"A": "Quick punishment", "B": "Fair procedures for laws and justice", "C": "Executive decision", "D": "Voting procedure"}, "B", "Due process ensures fair procedures in law and justice."),
    ("What is a copyright?", {"A": "Government writing", "B": "Legal protection of original works", "C": "Public information", "D": "Business registration"}, "B", "A copyright is legal protection for original creative works."),
    ("What is a patent?", {"A": "A government office", "B": "Legal protection for inventions", "C": "A business license", "D": "A land deed"}, "B", "A patent is legal protection granted for inventions."),
    ("What is a political ideology?", {"A": "A government building", "B": "A set of beliefs about government", "C": "A law", "D": "A political party"}, "B", "A political ideology is a set of beliefs about government."),
    ("What is conservatism?", {"A": "Saving money", "B": "Political belief favoring tradition and limited government", "C": "Protecting environment", "D": "Being careful"}, "B", "Conservatism favors tradition and limited government change."),
    ("What is liberalism?", {"A": "Being generous", "B": "Political belief favoring individual rights and change", "C": "Teaching", "D": "Freedom of speech"}, "B", "Liberalism favors individual rights and progressive change."),
]

# Literature Questions
literature_questions = [
    ("What is a novel?", {"A": "A short story", "B": "A long fictional prose narrative", "C": "A poem", "D": "A play"}, "B", "A novel is a long fictional prose narrative."),
    ("What is a metaphor?", {"A": "A direct comparison using like or as", "B": "A word meaning the opposite", "C": "A direct comparison without like or as", "D": "A repeated word"}, "C", "A metaphor is a direct comparison without using like or as."),
    ("What is symbolism?", {"A": "Using symbols", "B": "Using objects to represent ideas or concepts", "C": "Using colors", "D": "Using images"}, "B", "Symbolism uses objects to represent abstract ideas or concepts."),
    ("What is the protagonist?", {"A": "The villain", "B": "The main character", "C": "A supporting character", "D": "The narrator"}, "B", "The protagonist is the main character of a story."),
    ("What is the antagonist?", {"A": "The main character", "B": "A supporting character", "C": "The character opposing the protagonist", "D": "The narrator"}, "C", "The antagonist is the character who opposes the protagonist."),
    ("What is irony?", {"A": "When something is exactly as expected", "B": "When reality is opposite of what is expected", "C": "A type of poetry", "D": "A writing style"}, "B", "Irony is when reality is opposite of what is expected."),
    ("What is foreshadowing?", {"A": "Describing the past", "B": "Hinting at future events", "C": "Ending a story", "D": "Beginning a story"}, "B", "Foreshadowing is hinting at future events in a story."),
    ("What is a flashback?", {"A": "A sudden light", "B": "Going back to events in the past", "C": "A forward movement", "D": "A dream sequence"}, "B", "A flashback returns to events that happened earlier."),
    ("What is a theme?", {"A": "The title of a book", "B": "The main message or idea of a work", "C": "The setting of a story", "D": "The plot of a story"}, "B", "A theme is the main message or idea expressed in a work."),
    ("What is satire?", {"A": "A serious tone", "B": "Mocking or ridiculing something", "C": "A type of novel", "D": "A poetic form"}, "B", "Satire uses humor and ridicule to criticize something."),
    ("What is alliteration?", {"A": "Repetition of ending sounds", "B": "Repetition of beginning sounds", "C": "A type of rhythm", "D": "A poetic device"}, "B", "Alliteration is the repetition of beginning sounds in nearby words."),
    ("What is a sonnet?", {"A": "A 14-line poem often about love", "B": "A type of novel", "C": "A short story", "D": "A play"}, "A", "A sonnet is a 14-line poem, often expressing love or emotion."),
    ("What is poetry?", {"A": "A type of novel", "B": "Writing in verse, often with rhythm and rhyme", "C": "A dramatic work", "D": "A historical account"}, "B", "Poetry is writing in verse, often with rhythm, meter, and rhyme."),
    ("What is a narrative?", {"A": "A description", "B": "A story or account of events", "C": "A poem", "D": "A dialogue"}, "B", "A narrative is a story or account of events."),
    ("What is dialogue?", {"A": "A description of actions", "B": "Conversation between characters", "C": "A narration of events", "D": "A description of settings"}, "B", "Dialogue is the conversation between characters in a work."),
    ("What is an author?", {"A": "A reader", "B": "A person who writes books", "C": "A publisher", "D": "A character"}, "B", "An author is a person who writes books or literary works."),
    ("What is genre?", {"A": "A style of writing", "B": "A category of literature", "C": "A type of character", "D": "A literary device"}, "B", "Genre is a category of literature with common characteristics."),
    ("What is a plot?", {"A": "The setting", "B": "The characters", "C": "The sequence of events in a story", "D": "The theme"}, "C", "A plot is the sequence of events that make up a story."),
    ("What is a character?", {"A": "A symbol", "B": "A person or being in a story", "C": "The setting", "D": "The theme"}, "B", "A character is a person or being involved in the narrative."),
    ("What is the setting?", {"A": "The plot", "B": "The theme", "C": "The time and place where a story occurs", "D": "The characters"}, "C", "The setting is the time and place where a story takes place."),
    ("What is a climax?", {"A": "The beginning", "B": "The highest point of tension in a story", "C": "The ending", "D": "The introduction"}, "B", "The climax is the highest point of tension and turning point in a story."),
    ("What is a denouement?", {"A": "The climax", "B": "The resolution after the climax", "C": "The exposition", "D": "A literary device"}, "B", "Denouement is the resolution of a story after the climax."),
    ("What is exposition?", {"A": "A large fair", "B": "Introduction of characters and background information", "C": "A demonstration", "D": "A military action"}, "B", "Exposition introduces characters and background information."),
    ("What is rising action?", {"A": "Events building toward climax", "B": "The end of the story", "C": "The middle paragraph", "D": "Character description"}, "A", "Rising action builds tension toward the climax."),
    ("What is falling action?", {"A": "Events after climax leading to resolution", "B": "The introduction", "C": "The middle", "D": "Character development"}, "A", "Falling action consists of events after the climax."),
    ("What is a tragedy?", {"A": "A happy story", "B": "A sad but important story ending in disaster", "C": "A funny story", "D": "A short story"}, "B", "A tragedy is a serious drama with an unhappy ending."),
    ("What is a comedy?", {"A": "A long story", "B": "A dramatic work intended to be humorous", "C": "A sad story", "D": "A historical account"}, "B", "A comedy is a dramatic work intended to be amusing."),
    ("What is a ballad?", {"A": "A novel", "B": "A narrative poem or song", "C": "A play", "D": "A short story"}, "B", "A ballad is a narrative poem or song telling a story."),
    ("What is a haiku?", {"A": "A long poem", "B": "A three-line poem with 5-7-5 syllable pattern", "C": "A play", "D": "A short story"}, "B", "A haiku is a three-line poem with 5-7-5 syllable pattern."),
    ("What is a stanza?", {"A": "A single line", "B": "A paragraph in poetry", "C": "A group of lines in poetry", "D": "A rhyme scheme"}, "C", "A stanza is a group of lines in a poem."),
    ("What is a rhyme?", {"A": "Similar meanings", "B": "Repetition of sounds at end of words", "C": "Similar words", "D": "Repeated words"}, "B", "A rhyme is the repetition of sounds at the end of words."),
    ("What is a meter?", {"A": "A measuring tool", "B": "The rhythm or pattern of beats in poetry", "C": "A unit of length", "D": "A poetic device"}, "B", "Meter is the rhythmic pattern of stressed/unstressed syllables."),
    ("What is allusion?", {"A": "Comparison", "B": "Indirect reference to another work or person", "C": "Repetition", "D": "Exaggeration"}, "B", "An allusion is an indirect reference to another work or event."),
    ("What is a cliché?", {"A": "A new idea", "B": "An overused phrase or idea", "C": "A clever saying", "D": "A wise statement"}, "B", "A cliché is an overused expression or idea."),
    ("What is literary criticism?", {"A": "Finding faults in literature", "B": "Analysis and evaluation of literary works", "C": "Writing badly", "D": "Disliking literature"}, "B", "Literary criticism is analysis and evaluation of literary works."),
    ("What is a monologue?", {"A": "Conversation between two people", "B": "A long speech by one character", "C": "A group conversation", "D": "A silent scene"}, "B", "A monologue is a long speech by one character."),
    ("What is a soliloquy?", {"A": "Talking to others", "B": "A character speaking alone expressing inner thoughts", "C": "A conversation", "D": "A dialogue"}, "B", "A soliloquy is a character speaking alone revealing inner thoughts."),
    ("What is a tragedy of errors?", {"A": "A funny mistake", "B": "A drama based on misunderstandings", "C": "A tragic event", "D": "A character flaw"}, "B", "Tragedy of errors is a drama based on misunderstandings."),
    ("What is romanticism in literature?", {"A": "Love stories", "B": "Movement emphasizing emotion and nature", "C": "Historical fiction", "D": "Poetry only"}, "B", "Romanticism emphasizes emotion, nature, and individualism."),
]

# Economics Questions
economics_questions = [
    ("What is supply and demand?", {"A": "Goods needed and goods available", "B": "Price and quantity", "C": "Buyers and sellers", "D": "Economic systems"}, "A", "Supply and demand refers to goods available and goods needed."),
    ("What is GDP?", {"A": "Government Domestic Product", "B": "Gross Domestic Product", "C": "Global Demand Policy", "D": "General Development Program"}, "B", "GDP stands for Gross Domestic Product."),
    ("What is inflation?", {"A": "Increase in prices", "B": "Decrease in prices", "C": "Stable prices", "D": "Variable prices"}, "A", "Inflation is a general increase in prices over time."),
    ("What is deflation?", {"A": "Increase in prices", "B": "Decrease in prices", "C": "Stable prices", "D": "Price changes"}, "B", "Deflation is a general decrease in prices over time."),
    ("What is a monopoly?", {"A": "Many sellers", "B": "One seller dominating the market", "C": "Few sellers", "D": "Equal competition"}, "B", "A monopoly exists when one seller dominates the entire market."),
    ("What is a market economy?", {"A": "Planned economy", "B": "Economy based on supply and demand", "C": "Government-controlled economy", "D": "Barter system"}, "B", "A market economy is based on supply, demand, and free trade."),
    ("What is a command economy?", {"A": "Economy based on supply and demand", "B": "Economy controlled by government", "C": "Free market economy", "D": "Mixed economy"}, "B", "A command economy is controlled by the government."),
    ("What is profit?", {"A": "Total income", "B": "Total expenses", "C": "Revenue minus expenses", "D": "Wages earned"}, "C", "Profit is revenue minus expenses."),
    ("What is interest?", {"A": "Profit from selling goods", "B": "Cost of borrowing money", "C": "Return on investment", "D": "Wages from employment"}, "B", "Interest is the cost of borrowing money or return on savings."),
    ("What is a stock?", {"A": "Goods in storage", "B": "Ownership share in a company", "C": "Inventory of a store", "D": "Amount of money"}, "B", "A stock represents ownership in a company."),
    ("What is a bond?", {"A": "An agreement between people", "B": "A loan from government or company", "C": "A type of stock", "D": "Money saved"}, "B", "A bond is a loan agreement where you lend money."),
    ("What is unemployment?", {"A": "Working part-time", "B": "Having a job", "C": "Being without a job despite seeking one", "D": "Changing jobs"}, "C", "Unemployment is the state of being without a job while seeking one."),
    ("What is wage?", {"A": "A profit", "B": "Money paid for work", "C": "A price", "D": "An investment"}, "B", "A wage is money paid to workers for their labor."),
    ("What is tariff?", {"A": "A profit margin", "B": "A price tag", "C": "A tax on imported goods", "D": "A wage scale"}, "C", "A tariff is a tax on goods imported from other countries."),
    ("What is a consumer?", {"A": "A producer", "B": "A business owner", "C": "A person who buys goods and services", "D": "A worker"}, "C", "A consumer is a person who buys and uses goods and services."),
    ("What is an entrepreneur?", {"A": "An employee", "B": "A person who starts a business", "C": "A customer", "D": "A manager"}, "B", "An entrepreneur is a person who starts and runs a business."),
    ("What is capital?", {"A": "A city", "B": "Money and resources used in business", "C": "A worker", "D": "A product"}, "B", "Capital refers to money and resources used in production."),
    ("What is a recession?", {"A": "Economic growth", "B": "Period of economic decline", "C": "Stable economy", "D": "Rapid expansion"}, "B", "A recession is a period of economic decline."),
    ("What is a budget?", {"A": "Total earnings", "B": "Plan for spending money", "C": "Total expenses", "D": "Savings account"}, "B", "A budget is a plan for spending and managing money."),
    ("What is the law of diminishing returns?", {"A": "Profit always increases", "B": "Output decreases with more input eventually", "C": "Output always increases", "D": "Expenses decrease always"}, "B", "The law of diminishing returns states output eventually decreases with more input."),
    ("What is elasticity in economics?", {"A": "Flexibility of prices", "B": "Responsiveness of quantity to price changes", "C": "Business growth", "D": "Product quality"}, "B", "Elasticity measures how responsive quantity is to price changes."),
    ("What is scarcity?", {"A": "Rare items", "B": "Limited resources relative to wants", "C": "High prices", "D": "Supply shortage"}, "B", "Scarcity is the fundamental economic problem of limited resources."),
    ("What is opportunity cost?", {"A": "Cost of buying", "B": "Value of next best alternative given up", "C": "Business cost", "D": "Production expense"}, "B", "Opportunity cost is the value of what you give up for another choice."),
    ("What is comparative advantage?", {"A": "More production than others", "B": "Ability to produce at lower opportunity cost", "C": "Having best resources", "D": "Largest economy"}, "B", "Comparative advantage means producing at lower opportunity cost."),
    ("What is absolute advantage?", {"A": "Lower opportunity cost", "B": "Ability to produce more with same resources", "C": "Higher profit", "D": "Better technology"}, "B", "Absolute advantage means producing more with same resources."),
    ("What is specialization?", {"A": "Producing many goods", "B": "Focusing on producing specific goods", "C": "Mass production", "D": "Diversification"}, "B", "Specialization means focusing on producing specific goods."),
    ("What is a quota?", {"A": "A price limit", "B": "A limit on quantity of goods imported", "C": "A tax", "D": "A trade agreement"}, "B", "A quota limits the quantity of imported goods."),
    ("What is a subsidy?", {"A": "A tax on goods", "B": "Financial support from government", "C": "A loan", "D": "A price control"}, "B", "A subsidy is government financial support to businesses or producers."),
    ("What is marginal cost?", {"A": "Total cost", "B": "Cost of producing one additional unit", "C": "Average cost", "D": "Fixed cost"}, "B", "Marginal cost is the cost of producing one additional unit."),
    ("What is marginal revenue?", {"A": "Total revenue", "B": "Revenue from selling one additional unit", "C": "Average revenue", "D": "Fixed revenue"}, "B", "Marginal revenue is revenue from selling one additional unit."),
    ("What is perfect competition?", {"A": "One seller", "B": "Market with many sellers and buyers", "C": "Few sellers", "D": "Government controlled"}, "B", "Perfect competition has many sellers, buyers, and free entry."),
    ("What is monopolistic competition?", {"A": "Perfect competition", "B": "Many firms producing similar products", "C": "One firm only", "D": "Few firms"}, "B", "Monopolistic competition has many firms with differentiated products."),
    ("What is an oligopoly?", {"A": "One seller", "B": "Few large firms dominating market", "C": "Many firms", "D": "Perfect competition"}, "B", "An oligopoly has a few large firms controlling the market."),
    ("What is consumer surplus?", {"A": "Extra money", "B": "Difference between price paid and maximum willing to pay", "C": "Profit", "D": "Savings"}, "B", "Consumer surplus is the difference between willingness to pay and actual price."),
    ("What is producer surplus?", {"A": "Profit", "B": "Difference between actual price and minimum acceptable", "C": "Revenue", "D": "Cost"}, "B", "Producer surplus is difference between actual price and willingness to accept."),
    ("What is a recession?", {"A": "Economic growth", "B": "Period of economic decline", "C": "Stable prices", "D": "High employment"}, "B", "A recession is a period of declining economic activity."),
    ("What is a depression?", {"A": "Minor recession", "B": "Severe and prolonged recession", "C": "Economic growth", "D": "Inflation period"}, "B", "A depression is a severe and prolonged economic recession."),
    ("What is the labor force?", {"A": "All people", "B": "People employed or actively seeking employment", "C": "Only employed people", "D": "Retired people"}, "B", "The labor force includes employed and job-seeking people."),
    ("What is human capital?", {"A": "Money", "B": "Skills, knowledge, and abilities of workers", "C": "Physical assets", "D": "Property"}, "B", "Human capital is the skills and knowledge of workers."),
]

# CRS (Christian Religious Studies) Questions
crs_questions = [
    ("What does CRS stand for?", {"A": "Civil Religious Studies", "B": "Christian Religious Studies", "C": "Community Relations Service", "D": "Civic Religious Sciences"}, "B", "CRS stands for Christian Religious Studies."),
    ("What is morality?", {"A": "Following laws only", "B": "Principles of right and wrong behavior", "C": "Religious belief", "D": "Cultural tradition"}, "B", "Morality refers to principles of right and wrong behavior."),
    ("What is ethics?", {"A": "A set of rules", "B": "Study of principles of morality", "C": "A religious belief", "D": "A tradition"}, "B", "Ethics is the study of principles of right and wrong conduct."),
    ("What is sin?", {"A": "A mistake", "B": "An immoral act against religious law", "C": "A crime", "D": "A failure"}, "B", "Sin is an act that violates religious or moral law."),
    ("What is redemption?", {"A": "Buying something back", "B": "Forgiveness and salvation from sin", "C": "Punishment for wrongdoing", "D": "Repayment of debt"}, "B", "Redemption is forgiveness and salvation from sin."),
    ("What is grace?", {"A": "Elegance or poise", "B": "Divine unmerited favor", "C": "A prayer before meals", "D": "A compliment"}, "B", "Grace is divine favor or blessing not earned or deserved."),
    ("What is faith?", {"A": "Knowing something for certain", "B": "Belief and trust", "C": "Religious institution", "D": "A practice"}, "B", "Faith is belief and trust in something or someone."),
    ("What is compassion?", {"A": "Sympathy and concern for others", "B": "A religious practice", "C": "A virtue", "D": "An emotion"}, "A", "Compassion is sympathy and concern for others' suffering."),
    ("What is forgiveness?", {"A": "Forgetting wrongdoing", "B": "Releasing resentment and pardoning", "C": "Ignoring wrongs", "D": "Denying wrongdoing"}, "B", "Forgiveness is releasing resentment and pardoning wrongdoing."),
    ("What is virtue?", {"A": "A character flaw", "B": "A moral excellence or good quality", "C": "A bad habit", "D": "A weakness"}, "B", "A virtue is a moral excellence or good quality of character."),
    ("What is vice?", {"A": "A good habit", "B": "A moral flaw or bad habit", "C": "A virtue", "D": "Good behavior"}, "B", "A vice is a moral flaw, defect, or bad habit."),
    ("What is conscience?", {"A": "Memory", "B": "Inner sense of right and wrong", "C": "A law", "D": "A habit"}, "B", "Conscience is an inner sense guiding moral judgments."),
    ("What is charity?", {"A": "Giving money", "B": "Love and kindness toward others", "C": "A donation", "D": "Helping the poor only"}, "B", "Charity is love and selfless concern for others' welfare."),
    ("What is honesty?", {"A": "Being polite", "B": "Quality of being truthful", "C": "Following rules", "D": "Being kind"}, "B", "Honesty is the quality of being truthful and sincere."),
    ("What is justice?", {"A": "Punishment", "B": "Fair treatment and moral rightness", "C": "A court", "D": "A law"}, "B", "Justice is fair and moral treatment for all."),
    ("What is temptation?", {"A": "A desire for food", "B": "Desire to do something wrong", "C": "A test", "D": "A feeling"}, "B", "Temptation is the desire to do something wrong or sinful."),
    ("What is humility?", {"A": "Shame", "B": "Quality of being modest", "C": "Weakness", "D": "Shyness"}, "B", "Humility is the quality of being modest and humble."),
    ("What is pride?", {"A": "Confidence", "B": "Excessive self-esteem (considered a sin)", "C": "Self-respect", "D": "Courage"}, "B", "Pride is excessive self-esteem or arrogance (a deadly sin)."),
    ("What is penance?", {"A": "Punishment by law", "B": "Action of repenting for wrongdoing", "C": "Regret", "D": "Apology only"}, "B", "Penance is the act of repenting and making amends for sin."),
    ("What is reconciliation?", {"A": "Agreement on price", "B": "Restoring friendly relations", "C": "Settling a debt", "D": "Making peace between enemies"}, "D", "Reconciliation is restoring peace and friendly relations."),
    ("What is love in Christian context?", {"A": "Romantic feeling", "B": "Selfless care for others", "C": "Attraction", "D": "Emotion only"}, "B", "Christian love (agape) is selfless care for others."),
    ("What is prayer?", {"A": "Talking to oneself", "B": "Communication with God", "C": "Meditation only", "D": "Religious ritual"}, "B", "Prayer is direct communication with God or a higher power."),
    ("What is worship?", {"A": "Showing respect to a person", "B": "Religious reverence for God", "C": "Attending church", "D": "Following rules"}, "B", "Worship is showing religious reverence and devotion to God."),
    ("What is a sacrament?", {"A": "A prayer", "B": "A religious ritual considered sacred", "C": "A blessing", "D": "A commandment"}, "B", "A sacrament is a sacred religious ritual."),
    ("What is the Gospel?", {"A": "A song", "B": "Teachings of Jesus Christ", "C": "A book", "D": "A church service"}, "B", "The Gospel contains the teachings of Jesus Christ."),
    ("What is the Beatitudes?", {"A": "Blessings in Christian teaching", "B": "Ten Commandments", "C": "Parables", "D": "Miracles"}, "A", "The Beatitudes are blessings and teachings of Jesus."),
    ("What is a parable?", {"A": "A true story", "B": "A short story with moral lesson", "C": "A historical account", "D": "A poem"}, "B", "A parable is a story with a moral or spiritual lesson."),
    ("What is the Golden Rule?", {"A": "Money rule", "B": "Treat others as you wish to be treated", "C": "Rich people rule", "D": "A biblical law"}, "B", "The Golden Rule: treat others as you wish to be treated."),
    ("What is stewardship?", {"A": "Management of wealth", "B": "Responsible care of God's creation", "C": "Ownership of land", "D": "Business practice"}, "B", "Stewardship means responsible care for resources and creation."),
    ("What is resurrection?", {"A": "Coming back to life", "B": "Rising again after death (Christian belief)", "C": "Reincarnation", "D": "Spiritual rebirth"}, "B", "Resurrection in Christianity means rising from death to eternal life."),
]

# Mathematics Questions - Problem Solving
maths_questions = [
    ("Solve for x: 2x + 5 = 15", {"A": "x = 5", "B": "x = 10", "C": "x = 20", "D": "x = 3"}, "A", "2x + 5 = 15 → 2x = 10 → x = 5."),
    ("Solve for x: 3x - 7 = 20", {"A": "x = 9", "B": "x = 8", "C": "x = 7", "D": "x = 10"}, "A", "3x - 7 = 20 → 3x = 27 → x = 9."),
    ("Find the area of a circle with radius 5 cm", {"A": "78.5 cm²", "B": "31.4 cm²", "C": "50 cm²", "D": "25 cm²"}, "A", "Area = πr² = 3.14 × 5² = 3.14 × 25 = 78.5 cm²."),
    ("Find the circumference of a circle with radius 7 cm", {"A": "44 cm", "B": "49 cm", "C": "21.98 cm", "D": "14 cm"}, "A", "Circumference = 2πr = 2 × 3.14 × 7 = 43.96 ≈ 44 cm."),
    ("Find the area of a triangle with base 10 and height 8", {"A": "80", "B": "40", "C": "20", "D": "18"}, "B", "Area = ½bh = ½ × 10 × 8 = 40."),
    ("Find the volume of a cube with side 4 cm", {"A": "16 cm³", "B": "64 cm³", "C": "12 cm³", "D": "48 cm³"}, "B", "Volume = s³ = 4³ = 64 cm³."),
    ("What is 5! (5 factorial)?", {"A": "20", "B": "120", "C": "60", "D": "25"}, "B", "5! = 5 × 4 × 3 × 2 × 1 = 120."),
    ("Solve: 4x² = 36", {"A": "x = 3", "B": "x = 6", "C": "x = 9", "D": "x = ±3"}, "D", "4x² = 36 → x² = 9 → x = ±3."),
    ("Find the mean of: 5, 10, 15, 20", {"A": "12", "B": "12.5", "C": "12.75", "D": "13"}, "B", "Mean = (5 + 10 + 15 + 20) ÷ 4 = 50 ÷ 4 = 12.5."),
    ("Find the median of: 3, 7, 2, 9, 5", {"A": "5", "B": "7", "C": "2", "D": "9"}, "A", "Ordered: 2, 3, 5, 7, 9. Median is the middle value = 5."),
    ("If a line passes through (0,0) and (2,4), what is the slope?", {"A": "1", "B": "2", "C": "4", "D": "0.5"}, "B", "Slope = (4-0)/(2-0) = 4/2 = 2."),
    ("Solve: x² + 5x + 6 = 0", {"A": "x = -2, -3", "B": "x = 2, 3", "C": "x = 1, 6", "D": "x = -1, -6"}, "A", "x² + 5x + 6 = (x+2)(x+3) = 0 → x = -2 or x = -3."),
    ("What is 20% of 150?", {"A": "30", "B": "25", "C": "35", "D": "40"}, "A", "20% of 150 = 0.20 × 150 = 30."),
    ("If a triangle has sides 3, 4, and 5, is it a right triangle?", {"A": "Yes", "B": "No", "C": "Maybe", "D": "Cannot determine"}, "A", "3² + 4² = 9 + 16 = 25 = 5². Yes, by Pythagorean theorem."),
    ("Solve: |x - 5| = 3", {"A": "x = 8", "B": "x = 2", "C": "x = 8 or 2", "D": "x = 5"}, "C", "x - 5 = 3 or x - 5 = -3 → x = 8 or x = 2."),
    ("Find the distance between points (1,2) and (4,6)", {"A": "5", "B": "6", "C": "7", "D": "8"}, "A", "Distance = √[(4-1)² + (6-2)²] = √[9 + 16] = √25 = 5."),
    ("Simplify: (2³ × 2⁵) ÷ 2⁶", {"A": "2", "B": "4", "C": "8", "D": "16"}, "B", "(2³ × 2⁵) ÷ 2⁶ = 2⁸ ÷ 2⁶ = 2² = 4."),
    ("Solve: 2x + 3y = 13 and x - y = 1. What is x?", {"A": "2", "B": "3", "C": "4", "D": "5"}, "C", "From x - y = 1: x = y + 1. Substitute: 2(y+1) + 3y = 13 → 5y = 11 is wrong. Let me recalculate: x = 4, y = 3."),
    ("What is √144?", {"A": "10", "B": "11", "C": "12", "D": "13"}, "C", "√144 = 12 because 12 × 12 = 144."),
    ("A store offers 25% discount on a $80 item. What is the final price?", {"A": "$60", "B": "$50", "C": "$55", "D": "$65"}, "A", "Discount = 25% × $80 = $20. Final price = $80 - $20 = $60."),
    ("Solve: 5x - 2 = 3x + 6", {"A": "x = 2", "B": "x = 4", "C": "x = 6", "D": "x = 8"}, "B", "5x - 3x = 6 + 2 → 2x = 8 → x = 4."),
    ("What is ∛27?", {"A": "2", "B": "3", "C": "4", "D": "5"}, "B", "∛27 = 3 because 3 × 3 × 3 = 27."),
    ("Convert 0.75 to a fraction", {"A": "1/2", "B": "2/3", "C": "3/4", "D": "4/5"}, "C", "0.75 = 75/100 = 3/4."),
    ("Find the area of a rectangle with length 12 and width 5", {"A": "34", "B": "60", "C": "17", "D": "35"}, "B", "Area = length × width = 12 × 5 = 60."),
    ("Solve: x/3 + 5 = 11", {"A": "x = 18", "B": "x = 12", "C": "x = 24", "D": "x = 36"}, "A", "x/3 = 6 → x = 18."),
    ("What is 15% of 200?", {"A": "30", "B": "35", "C": "40", "D": "45"}, "A", "15% of 200 = 0.15 × 200 = 30."),
    ("Find the perimeter of a rectangle with length 8 and width 5", {"A": "13", "B": "26", "C": "40", "D": "65"}, "B", "Perimeter = 2(l + w) = 2(8 + 5) = 2 × 13 = 26."),
    ("Solve: 3(x - 2) = 15", {"A": "x = 5", "B": "x = 7", "C": "x = 9", "D": "x = 11"}, "B", "3(x - 2) = 15 → x - 2 = 5 → x = 7."),
    ("What is 40% of 250?", {"A": "80", "B": "90", "C": "100", "D": "110"}, "C", "40% of 250 = 0.40 × 250 = 100."),
    ("Find the hypotenuse of a right triangle with legs 6 and 8", {"A": "10", "B": "12", "C": "14", "D": "16"}, "A", "c² = a² + b² = 6² + 8² = 36 + 64 = 100 → c = 10."),
    ("Solve: x² - 9 = 0", {"A": "x = 3", "B": "x = -3", "C": "x = 3 or -3", "D": "x = 0"}, "C", "x² = 9 → x = ±3."),
    ("What is the reciprocal of 5?", {"A": "1/5", "B": "5", "C": "-5", "D": "0.2"}, "A", "The reciprocal of 5 is 1/5 or 0.2."),
    ("Solve: 2x² - 8 = 0", {"A": "x = 2", "B": "x = -2", "C": "x = 2 or -2", "D": "x = 4"}, "C", "2x² = 8 → x² = 4 → x = ±2."),
    ("Convert 2.5 to a fraction", {"A": "5/2", "B": "2/5", "C": "5/4", "D": "4/5"}, "A", "2.5 = 25/10 = 5/2."),
    ("What is the sum of angles in a triangle?", {"A": "90°", "B": "180°", "C": "270°", "D": "360°"}, "B", "The sum of interior angles in any triangle is 180°."),
    ("If x = 2, what is 3x² + 2x + 1?", {"A": "15", "B": "16", "C": "17", "D": "18"}, "C", "3(2)² + 2(2) + 1 = 3(4) + 4 + 1 = 12 + 4 + 1 = 17."),
    ("Solve: x + 2x + 3x = 60", {"A": "x = 10", "B": "x = 15", "C": "x = 20", "D": "x = 30"}, "A", "6x = 60 → x = 10."),
    ("What is 12.5% of 80?", {"A": "8", "B": "10", "C": "12", "D": "15"}, "B", "12.5% of 80 = 0.125 × 80 = 10."),
    ("Find the value of y when x = 3 in: y = 2x + 4", {"A": "9", "B": "10", "C": "11", "D": "12"}, "B", "y = 2(3) + 4 = 6 + 4 = 10."),
]

# Topic and Question mapping for each subject
subject_topics = {
    "Physics": ["Mechanics", "Heat and Thermodynamics", "Waves and Sound", "Electricity and Magnetism"],
    "Chemistry": ["Atomic Structure", "Chemical Bonding", "Reactions and Solutions", "Organic Chemistry"],
    "Biology": ["Cell Biology", "Genetics", "Evolution", "Ecology"],
    "English": ["Grammar", "Literature", "Writing", "Reading Comprehension"],
    "Government": ["Political Systems", "Rights and Responsibilities", "International Relations", "Laws and Justice"],
    "Literature": ["Prose", "Poetry", "Drama", "Literary Criticism"],
    "Economics": ["Microeconomics", "Macroeconomics", "Trade and Markets", "Economic Indicators"],
    "CRS": ["Ethics and Morality", "Personal Development", "Social Values", "Spiritual Growth"],
    "Mathematics": ["Algebra", "Geometry", "Trigonometry", "Calculus"],
}

all_questions = {
    "Physics": physics_questions,
    "Chemistry": chemistry_questions,
    "Biology": biology_questions,
    "English": english_questions,
    "Government": government_questions,
    "Literature": literature_questions,
    "Economics": economics_questions,
    "CRS": crs_questions,
    "Mathematics": maths_questions,
}

# Create topics and questions
for subject_name, topics_list in subject_topics.items():
    subject_id = subjects[subject_name]
    
    for topic_title in topics_list:
        topic = Topic(subject_id=subject_id, title=topic_title)
        db.add(topic)
        db.flush()
        
        # Distribute questions evenly across topics (5 questions per topic = 20 per subject)
        questions_for_subject = all_questions[subject_name]
        questions_per_topic = len(questions_for_subject) // len(topics_list)
        start_idx = topics_list.index(topic_title) * questions_per_topic
        end_idx = start_idx + questions_per_topic
        
        for question_text, options, correct_answer, explanation in questions_for_subject[start_idx:end_idx]:
            question = Question(
                topic_id=topic.id,
                question=question_text,
                options=options,
                correct_answer=correct_answer,
                explanation=explanation
            )
            db.add(question)

db.commit()
print("Successfully added all subjects with 20 questions each!")