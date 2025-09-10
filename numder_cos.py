import numpy as np
import matplotlib.pyplot as plt

def dcos_true(t):
    return -np.sin(t)

def fd_cos(t,h):
    val = (np.cos(t+h) - np.cos(t) ) / h
    return val

def cd_cos(t,h):
    val = (np.cos(t+h/2) - np.cos(t-h/2) ) / h
    return val

def ed_cos(t,h):
    val = (8*( np.cos(t+h/4) - np.cos(t-h/4) ) - ( np.cos(t+h/2) - np.cos(t-h/2) ))/3/h
    return val

def rel_error(approx, true):
    return np.abs((approx - true)/true) 

if __name__ == "__main__":

    t_val=[0.1,1,100]

    fig, axs = plt.subplots(2,3, gridspec_kw={'height_ratios':[1.5,2]}, figsize=(20,10))

    # initialize values and empty lists in preparation
    for i,t in enumerate(t_val):
        true_cos_val = dcos_true(t)
        h_vals = []
        fd_cos_vals, cd_cos_vals, ed_cos_vals = [],[],[]
        fd_cos_errs, cd_cos_errs, ed_cos_errs = [],[],[]

        h=1.0 # initializes h for next nested loop

        for h in np.logspace(-16, 0.5, 500): # logspace makes the iteration space nicer. lowest value should be machine precision for a 64-bit float
            h_vals.append(h)

            fd_cos_vals.append(fd_cos(t,h))
            cd_cos_vals.append(cd_cos(t,h))
            ed_cos_vals.append(ed_cos(t,h))

            fd_cos_errs.append(rel_error(fd_cos(t,h),true_cos_val))
            cd_cos_errs.append(rel_error(cd_cos(t,h),true_cos_val))
            ed_cos_errs.append(rel_error(ed_cos(t,h),true_cos_val))

            h/2 # makes h smaller for next loop

        # promote lists to np arrays
        h_vals=np.array(h_vals)

        fd_cos_vals=np.array(fd_cos_vals)
        cd_cos_vals=np.array(cd_cos_vals)
        ed_cos_vals=np.array(ed_cos_vals)

        fd_cos_errs=np.array(fd_cos_errs)
        cd_cos_errs=np.array(cd_cos_errs)
        ed_cos_errs=np.array(ed_cos_errs)

        # BEGIN PLOTS

        # top row
        ax_top = axs[0,i] #give name for simplicity
        ax_top.xaxis.grid(True)
        ax_top.yaxis.grid(True)
        ax_top.axhline(true_cos_val, c='r', lw=1, linestyle="-", label='True' )
        ax_top.plot(h_vals, fd_cos_vals, c='g', ls='--', label='Forward')
        ax_top.plot(h_vals, cd_cos_vals, c='b', ls=':', label='Central')
        ax_top.plot(h_vals, ed_cos_vals, c='m', ls='-.', label='Extrapolated')
        ax_top.set_xscale('log')
        ax_top.set_ylabel(r"$\frac{d}{dt}[\cos(t)]$", fontsize=14)
        ax_top.set_title(f"t={t}")
        ax_top.legend()

        #bottom row
        ax_bot = axs[1,i]
        ax_bot.xaxis.grid(True)
        ax_bot.yaxis.grid(True)
        ax_bot.plot(h_vals, fd_cos_errs, c='g', ls='--', label='Forward')
        ax_bot.plot(h_vals, cd_cos_errs, c='b', ls=':', label='Central')
        ax_bot.plot(h_vals, ed_cos_errs, c='m', ls='-.', label='Extrapolated')
        ax_bot.set_xscale('log')
        ax_bot.set_yscale('log')
        ax_bot.set_xlabel('h', fontsize=15)
        ax_bot.set_ylabel(r'$\varepsilon_{rel}$', fontsize=20)
        ax_bot.legend()

    plt.savefig("cos.png",dpi=300)