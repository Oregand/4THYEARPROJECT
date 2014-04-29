//
//  HyundaiViewController.m
//  DealzFrontEnd2
//
//  Created by David O'Regan on 18/03/2014.
//  Copyright (c) 2014 David O'Regan. All rights reserved.
//

#import "HyundaiViewController.h"
#import "Cars.h"
#import "DetailViewController.h"

#define getDataUrl @"http://localhost:8888/josn2.php"

@interface HyundaiViewController ()

@end

@implementation HyundaiViewController
@synthesize jsonArray, carArray;

- (id)initWithStyle:(UITableViewStyle)style
{
    self = [super initWithStyle:style];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    //Set the title of our view loader
    self.title = @"Cars of the world!";
    
    //Load data like a bauce
    [self retriveData];
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - Table view data source

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    // Return the number of sections.
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    // Return the number of rows in the section.
    return carArray.count;
}


- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{

    static NSString * CellIdentifier = @ "Cell";
    UITableViewCell * cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier forIndexPath:indexPath];
    
    // Configure the cell...
    Cars * carObject;
    carObject = [carArray objectAtIndex:indexPath.row];
    
    cell.textLabel.text = carObject.title;
    
    cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator;
    return cell;
}


/*
// Override to support conditional editing of the table view.
- (BOOL)tableView:(UITableView *)tableView canEditRowAtIndexPath:(NSIndexPath *)indexPath
{
    // Return NO if you do not want the specified item to be editable.
    return YES;
}
*/

/*
// Override to support editing the table view.
- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath
{
    if (editingStyle == UITableViewCellEditingStyleDelete) {
        // Delete the row from the data source
        [tableView deleteRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationFade];
    } else if (editingStyle == UITableViewCellEditingStyleInsert) {
        // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
    }   
}
*/

/*
// Override to support rearranging the table view.
- (void)tableView:(UITableView *)tableView moveRowAtIndexPath:(NSIndexPath *)fromIndexPath toIndexPath:(NSIndexPath *)toIndexPath
{
}
*/

/*
// Override to support conditional rearranging of the table view.
- (BOOL)tableView:(UITableView *)tableView canMoveRowAtIndexPath:(NSIndexPath *)indexPath
{
    // Return NO if you do not want the item to be re-orderable.
    return YES;
}
*/


#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
    
    if ([[segue identifier] isEqualToString:@"pushDetailView"])
    {
        NSIndexPath * indexPath = [self.tableView indexPathForSelectedRow];
        
        //Get the object for selcted row
        Cars * object = [carArray objectAtIndex:indexPath.row];
        
        [[segue destinationViewController] getCar:object];
    }
}




#pragma mark -
#pragma mark Class Methods

- (void) retriveData
{
    
    NSError* error;
    
    NSURL * url = [NSURL URLWithString:getDataUrl];
    NSData * data = [NSData dataWithContentsOfURL:url];
    NSString *result = [[NSString alloc] initWithData:data encoding:NSASCIIStringEncoding];

//    NSString *someString = [[NSString alloc] initWithData:data encoding:NSASCIIStringEncoding];
//    NSLog(@"Data Value: + %@",data);

    // = [[NSData alloc] init];
    //data = [NSData dataWithContentsOfURL:url];
    
    jsonArray = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:&error];
    
    //Set up our cars object
    carArray = [[NSMutableArray alloc] init];
    
    //Loop through our json array
    for(int i = 0; i < jsonArray.count; i++)
    {
        //Create our car object
        NSString * cTitle = [[jsonArray objectAtIndex:i] objectForKey:@"title"];
        NSString * cLink = [[jsonArray objectAtIndex:i] objectForKey:@"link"];
        NSString * cPrice = [[jsonArray objectAtIndex:i] objectForKey:@"price"];
        NSString * cYear = [[jsonArray objectAtIndex:i] objectForKey:@"carYear"];
        NSString * cLocation = [[jsonArray objectAtIndex:i] objectForKey:@"location"];
        NSString * cMileage = [[jsonArray objectAtIndex:i] objectForKey:@"mileage"];
        NSString * cEngine = [[jsonArray objectAtIndex:i] objectForKey:@"engine"];

        
        //Add car object to our car array
        [carArray addObject:[[Cars alloc] initWithTitle:cTitle andLink:cLink andCarYear:cYear andPrice:cPrice andLocation:cLocation andMileage:cMileage andEngine:cEngine]];
         }
         //reload our for loop
         [self.tableView reloadData];
}
@end
